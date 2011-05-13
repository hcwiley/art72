ssh wd40too@wd40too.com <<'ENDSSH'
cd /home/wd40too/hg/hcwiley-django/
hg pull
hg up
cp -r portfolio/* /home/wd40too/webapps/hcw_dj/portfolio/
cp -r public/* /home/wd40too/webapps/hcw_dj_static/
cd /home/wd40too/webapps/hcw_dj/apache2/bin
./restart
exit
ENDSSH
