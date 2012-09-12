from django.conf import settings
from django.db import models
from django.template.base import Template
from django.template.context import Context
from sorl import thumbnail
from django.template.loader import get_template
import Image
from apps.theme.utils import Point, get_point_on_circle
import math
from django.core.exceptions import ValidationError

class ColorPalette(models.Model):
    """
    A color palette consisting of 5 hex colors as used in CSS e.g. #abcdef.
    #TODO: make a HexColorField
    #TODO: do some rounding on the svgs before passing it off to the js
    """
    c1 = models.CharField(max_length=7)
    c2 = models.CharField(max_length=7)
    c3 = models.CharField(max_length=7)
    c4 = models.CharField(max_length=7)
    c5 = models.CharField(max_length=7)

    def as_context_data(self):
        """
        Returns the 5 CSS ready colors as a dictionary for use as Context data.
        e.g.
        {'c1': u'#aabbcc', 'c2': u'#aaa', 'c3': u'#fff', 'c4': u'#fff', 'c5': u'#fff'}
        """
        data = {}
        for x in range(1, 6):
            field_name = 'c%d' % x
            data[field_name] = getattr(self, field_name)
        return data
    
    def as_wheel(self, width=128):
        """
        Returns a SVG color wheel of specified width.
        e.g.
        <svg xmlns='http://www.w3.org/2000/svg' version='1.1' >
            <!-- border -->
            <circle cx='64.0' cy='64.0' r='61.44' 
            . . .
            <path d='M, L, a, 0 0,0 ,' />
        </svg>
        """
        # some intial settings, these can be changed freely
        border_color = "#888"       # color of circular border
        border_width_percent = 4    # border width as a percent of width
        border_gap_percent = 8      # gap between border and wheel
        slice_gap_degrees = 12      # arc of gap at radius between slices 
        ccw = False                 # whether c1-c5 go counter clock wise
        
        radius = width / 2.0
        border_width = border_width_percent * width / 100.0
        border_gap = border_gap_percent * width / 100.0
        # drawing at 0,0 so the origin is the radius
        origin = Point(radius, radius)
        # border is drawn with circle's stroke - account for extra width 
        radius -= border_width / 2.0
        # ColorPalette has 5 colors
        slices = 5
        gap_radian = math.radians(slice_gap_degrees)
        arc_radian = 2 * math.pi / slices - gap_radian
        half_arc = arc_radian / 2.0 
        c = {
             'center': origin,
             'radius': radius,
             'border_color': border_color,
             'border_width': border_width,
        }
        # calculate inner circle - account for border gap
        radius -= border_gap + border_width / 2.0
        # arc radians of first color
        arc1 = half_arc - math.pi / 2.0
        # calculate each color
        for x in range(1, 6):
            arc2 = arc1 - arc_radian
            field_name = 'c%d' % x
            val = getattr(self, field_name)
            # arc points
            p1 = get_point_on_circle(origin.x, radius, arc1)
            p2 = get_point_on_circle(origin.x, radius, arc2)
            # radian half way between arc 1 and 2
            mid_arc = (arc1 + arc2) / 2.0
            
            # i'm not sure why this calculation works, but it does -z
            # alternatively take the difference of the heights of the 
            # two isosceles triangles (the one shown and sans gaps)
            offset = width * slice_gap_degrees / 100.0 / 2.0
            start = get_point_on_circle(origin.x, offset, mid_arc) 
            c[field_name] = {
                                'start': start,
                                'radius': radius,
                                'arc_point': p1,
                                'arc_delta': Point((p2.x - p1.x), (p2.y - p1.y)),
                                'color': val,
                            } 
            if ccw:
                arc1 = arc2 - gap_radian
            else:
                arc1 += arc_radian + gap_radian
        t = get_template('theme/color-wheel.svg')
        return t.render(Context(c))
    
    def clean(self):
        """Ensures this is a valid CSS color."""
        for x in range(1, 6):
            field_name = 'c%d' % x
            val = getattr(self, field_name)
            no_pound = val
            # get rid of leading '#' for hex parsing
            if val.startswith('#'):
                no_pound= val[1:]
            # it should now be 6 or 3 e.g. abcdef, fff     
            count = len(no_pound)
            if count != 6 and count != 3:
                raise ValidationError('A valid CSS color must have either 3 or 6 hex values, got %d instead.' % count)
            # hex values should be hex values
            try:
                print int(no_pound, 16)
            except ValueError:
                raise ValidationError('%s is not base 16 and therefore not a valid CSS color. Only use 0-9 and a-f (case-insensitive)' % no_pound)
    
    def save(self, *args, **kwargs):
        """Adds a '#' if missing and then saves."""
        for x in range(1, 6):
            field_name = 'c%d' % x
            val = getattr(self, field_name)
            if not val.startswith('#'):
                setattr(self, field_name, u'#' + val)
        super(ColorPalette, self).save(*args, **kwargs)  
        
    def __unicode__(self):
        return "ColorPalette " + str(self.pk) 
        
class TypeKitFont(models.Model):
    """
    Represents a font from the TypeKit service. https://typekit.com/
    title: human readable font title e.g. FF Meta Web Pro
    typekit: TypeKit css font-family. e.g. ff-meta-web-pro
    """
    title = models.CharField(max_length=50, unique=True, help_text="The font title. e.g. FF Meta Web Pro")
    typekit = models.SlugField(max_length=50, unique=True, help_text="The typekit css font-family. e.g. ff-meta-web-pro")

    def __unicode__(self):
        return self.title[0].upper() + self.title[1:]
    
class FontPair(models.Model):
    """
    A fine pairing of fonts. Like cheese and wine, but with more serifs (or not).
    """
    f1 = models.ForeignKey(TypeKitFont, related_name='%(app_label)s_%(class)s_f1')
    f2 = models.ForeignKey(TypeKitFont, related_name='%(app_label)s_%(class)s_f2')

    def __unicode__(self):
        return u"%s & %s" % (self.f1.__unicode__(), self.f2.__unicode__())
    
    def as_context_data(self):
        """
        Returns the 2 CSS ready fonts as a dictionary for use as Context data.
        e.g.
        {'f1': u'ff-meta-web-pro', 'f2': u'adelle'}
        """
        return { 'f1' : self.f1.typekit, 'f2' : self.f2.typekit }
    
    class Meta:
        unique_together = ('f1', 'f2') 

# no magic numbers plzkthx
SITE = 0
PIECE = 1
SERIES = 2
CATEGORY = 3

class SiteLayoutManager(models.Manager):
    """Returns only the Layouts with SITE depth"""
    def get_query_set(self):
        return super(SiteLayoutManager, self).get_query_set().filter(depth=SITE)

class PieceLayoutManager(models.Manager):
    """Returns only the Layouts with PIECE depth"""
    def get_query_set(self):
        return super(PieceLayoutManager, self).get_query_set().filter(depth=PIECE)

class SeriesLayoutManager(models.Manager):
    """Returns only the Layouts with SERIES depth"""
    def get_query_set(self):
        return super(SeriesLayoutManager, self).get_query_set().filter(depth=SERIES)

class CategoryLayoutManager(models.Manager):
    """Returns only the Layouts with CATEGORY depth"""
    def get_query_set(self):
        return super(CategoryLayoutManager, self).get_query_set().filter(depth=CATEGORY)


class Layout(models.Model):
    DEPTH_CHOICES = (
        (SITE, 'Site'),
        (PIECE, 'Piece'),
        (SERIES, 'Series'),
        (CATEGORY, 'Category'),
    )
    title = models.CharField(max_length=50)
    depth = models.SmallIntegerField(choices=DEPTH_CHOICES)
    css_template = models.TextField(help_text="A css django template.<br />Reference theme colors with {{ c1 }}, {{ c2 }} ... {{ c5 }}.<br />Reference theme fonts with {{ primary_font }} and {{ secondary_font }}.")
    icon = thumbnail.ImageField(upload_to='images/layouts')
    description = models.TextField()
    image_dimension = models.CharField(max_length=12, blank=True, null=True)
    thumb_dimension = models.CharField(max_length=12, blank=True, null=True)
    supports_background_image = models.BooleanField(default=False)
    objects = models.Manager()
    site_objects = SiteLayoutManager()
    piece_objects = PieceLayoutManager()
    series_objects = SeriesLayoutManager()
    category_objects = CategoryLayoutManager() 
    #defaul both to 200x200
    def as_template(self):
        return Template(self.css_template)
    
    def __unicode__(self):
        return self.title
    
    def image_width(self):
        return self.image_dimension.split('x')[0]
    
    def image_height(self):
        return self.image_dimension.split('x')[1]
    

try:
    MAX_IMAGE_SIZE = settings.MAX_IMAGE_SIZE 
except AttributeError:
    MAX_IMAGE_SIZE = (1400, 1400) 

#TODO: default theme/color/etc for new users
class Theme(models.Model):
    DEPTH_CHOICES = (
        (PIECE, 'Piece'),
        (SERIES, 'Series'),
        (CATEGORY, 'Category'),
    )
    colors = models.ForeignKey(ColorPalette)
    fonts = models.ForeignKey(FontPair)
    depth = models.SmallIntegerField(choices=DEPTH_CHOICES)
    site_layout = models.ForeignKey(Layout, related_name='%(app_label)s_%(class)s_site_layout')
    piece_layout = models.ForeignKey(Layout, related_name='%(app_label)s_%(class)s_piece_layout')
    series_layout = models.ForeignKey(Layout, related_name='%(app_label)s_%(class)s_series_layout', blank=True, null=True)
    category_layout = models.ForeignKey(Layout, related_name='%(app_label)s_%(class)s_category_layout', blank=True, null=True)
    background_image = thumbnail.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
#TODO: validate that each layout has the appropriate DEPTH_CHOICE - limit selection
#TODO: also validate that the series/category layouts are there when called for by the site depth
    
    def get_template(self):
        return self.site_layout.as_template()
    
    def get_context(self):
        c = Context(self.fonts.as_context_data())
        c.update(self.colors.as_context_data())
        return c
    
    def piece_css(self):
        return self.piece_layout.as_template().render(self.get_context())
    
    def series_css(self):
        return self.series_layout.as_template().render(self.get_context())
    
    def category_css(self):
        return self.category_layout.as_template().render(self.get_context())
    
    def render_css(self):
        #TODO: compress and cache on server - maybe even move to a textfield
        return self.get_template().render(self.get_context())

    def do_resizes(self):
        """
        Only allow images to be MAX_IMAGE_SIZE.
        """
        if self.background_image:
            img = Image.open(self.background_image.path)
            img.thumbnail(MAX_IMAGE_SIZE, Image.ANTIALIAS)
            img.save(self.background_image.path)
        
    def __unicode__(self):
        #TODO: how to access OneToOne Artist relationship here to put in __unicode__
        return u"Theme %d" % self.pk
    
    def save(self, *args, **kwargs):
        """Save then do any needed image resiziging."""
        super(Theme, self).save(*args, **kwargs)
        self.do_resizes()
