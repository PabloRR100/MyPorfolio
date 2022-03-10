###
# After running docker-compose up, interact directly with postgres with:
# docker-compose exec db psql -U pruizruiz
# \l   --> To list databases
###

# pull official base image
FROM postgres:14-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
