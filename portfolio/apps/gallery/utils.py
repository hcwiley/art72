from django.template.defaultfilters import slugify

def get_default_slug(title, max_length):
    slug = slugify(title)

    if len(slug) > max_length:
        slug = slug[:max_length]
        
    return slug

def get_unique_slug(query_set, title, max_length):    
    orig_slug = slug = get_default_slug(title, max_length)
    count = 1
    delimiter = '-'
    
    while query_set.filter(slug=slug).exists():
        count += 1
        padding = delimiter + str(count)
        
        if len(orig_slug) + len(padding) > max_length:
            orig_slug = orig_slug[:max_length - len(padding)]
        
        slug = orig_slug + padding
    
    return slug

#    """
#    Gets a unique slug based off the title.
#    The slug is unique for the provided query_set and is at most max_length.
#    
#    It first slugifies the title, then truncates the resulting slug if needed.
#    Once slugified and truncated it is then compared against query_set.
#    If another match is found, a count is either appended or incremented and
#    again checked for max_length until a unique slug is obtained.
#    
#    e.g.
#    If a piece is saved with title "foo bar", the first slug will be "foo-bar".
#    The next piece saved which results in the same slug will be incremented 
#    and will result in the slug "foo-bar-2", the next "foo-bar-3", etc.
#    
#    * This does not account for numbers being in the original title.
#    If a piece with the title "foo bar 42" is added, the first slug will be 
#    "foo-bar-42" and the next matching slug will be "foo-bar-43".
#    """
## keep changing the slug until it is unique
#while True:
#    # find instances with same slug
#    lookups = dict(default_lookups, **{field.name: slug})
#    rivals = manager.filter(**lookups).exclude(pk=instance.pk)
#
#    if not rivals:
#        # the slug is unique, no model uses it
#        return slug
#
#    # the slug is not unique; change once more
#    index += 1
#
#    # ensure the resulting string is not too long
#    tail_length = len(field.index_sep) + len(str(index))
#    combined_length = len(original_slug) + tail_length
#    if field.max_length < combined_length:
#        original_slug = original_slug[:field.max_length - tail_length]
#
#    # re-generate the slug
#    data = dict(slug=original_slug, sep=field.index_sep, index=index)
#    slug = '%(slug)s%(sep)s%(index)d' % data
#
#    # ...next iteration...



