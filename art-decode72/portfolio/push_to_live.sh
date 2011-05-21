ssh wd40too@wd40too.com <<'ENDSSH'
cd /home/wd40too/hg/artist-sites/
hg pull
hg up
cp -r art-decode72/portfolio/* /home/wd40too/webapps/artist_sites/portfolio/
cp -r art-decode72/public/* /home/wd40too/webapps/artist_sites_static/
cd /home/wd40too/webapps/artist_sites/apache2/bin
./restart
exit
ENDSSH
