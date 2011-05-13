#ssh hcwiley@hcwiley.com
cp -r ~/webapps/hcw_dj/portfolio/* /home/hcwiley/hg/hcwiley-django/portfolio/
cp -r ~/webapps/hcw_dj_static/* /home/hcwiley/hg/hcwiley-django/public/
cd  /home/hcwiley/hg/hcwiley-django/
hg ci -m 'commit from live'
hg push

