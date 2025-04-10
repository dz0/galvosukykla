dates  = """
2013-03-03
2013-03-03
2013-03-02
2013-03-02
2013-03-01
2013-03-01
2013-02-28
2013-02-28
2013-02-27
2013-02-27
2013-02-26
2013-02-25
2013-02-25
2013-02-24
2013-02-24
2013-02-23
2013-02-23
2013-02-22
2013-02-22
2013-02-21
2013-02-21
2013-02-20
2013-02-20
2013-02-19
2013-02-19
2013-02-18
2013-02-17
2013-01-23
2013-01-23
2013-01-22
2013-01-22
2013-01-21
2013-01-21
2013-01-20
2013-01-20
2013-01-19
2013-01-19
2013-01-18
2013-01-18
2013-01-17
2013-01-17
2013-01-16
2013-01-16
2013-01-15
2013-01-15
2013-01-14
2013-01-14
2013-01-13
2013-01-13
2013-01-11
2013-01-10
2013-01-10
2013-01-09
2013-01-09
2013-01-08
2013-01-08
2013-01-07
2013-01-07
2012-12-31
2012-12-27
2012-12-27
2012-12-26
2012-12-26
2012-12-23
""".split('\n')

dates =  list(set(dates))
dates.sort()

#~ for date in dates:
    #~ print ('http://galvosukykla.wordpress.com/%s/%s/' % (date, date) )
#~ 
#~ 
'http://galvosukykla.wordpress.com/2012/12/18/2012-12-18/'
year = 2012
for month in range(12, 13):
    for day in range(1, 31):
        print ('http://galvosukykla.wordpress.com/%(year)s/%(month)02d/%(day)02d/%(year)s-%(month)02d-%(day)02d/' % locals() )

http://galvosukykla.wordpress.com/2012/12/19/2012-12-19/
http://galvosukykla.wordpress.com/2012/12/20/2012-12-20/
http://galvosukykla.wordpress.com/2012/12/21/2012-12-21/
http://galvosukykla.wordpress.com/2012/12/22/2012-12-22/
http://galvosukykla.wordpress.com/2012-12-23/2012-12-23/
http://galvosukykla.wordpress.com/2012-12-26/2012-12-26/
http://galvosukykla.wordpress.com/2012-12-27/2012-12-27/
http://galvosukykla.wordpress.com/2012-12-31/2012-12-31/
http://galvosukykla.wordpress.com/2013-01-07/2013-01-07/
http://galvosukykla.wordpress.com/2013-01-08/2013-01-08/
http://galvosukykla.wordpress.com/2013-01-09/2013-01-09/
http://galvosukykla.wordpress.com/2013-01-10/2013-01-10/
http://galvosukykla.wordpress.com/2013-01-11/2013-01-11/
http://galvosukykla.wordpress.com/2013-01-13/2013-01-13/
http://galvosukykla.wordpress.com/2013-01-14/2013-01-14/
http://galvosukykla.wordpress.com/2013-01-15/2013-01-15/
http://galvosukykla.wordpress.com/2013-01-16/2013-01-16/
http://galvosukykla.wordpress.com/2013-01-17/2013-01-17/
http://galvosukykla.wordpress.com/2013-01-18/2013-01-18/
http://galvosukykla.wordpress.com/2013-01-19/2013-01-19/
http://galvosukykla.wordpress.com/2013-01-20/2013-01-20/
http://galvosukykla.wordpress.com/2013-01-21/2013-01-21/
http://galvosukykla.wordpress.com/2013-01-22/2013-01-22/
http://galvosukykla.wordpress.com/2013-01-23/2013-01-23/
http://galvosukykla.wordpress.com/2013-02-17/2013-02-17/
http://galvosukykla.wordpress.com/2013-02-18/2013-02-18/
http://galvosukykla.wordpress.com/2013-02-19/2013-02-19/
http://galvosukykla.wordpress.com/2013-02-20/2013-02-20/
http://galvosukykla.wordpress.com/2013-02-21/2013-02-21/
http://galvosukykla.wordpress.com/2013-02-22/2013-02-22/
http://galvosukykla.wordpress.com/2013-02-23/2013-02-23/
http://galvosukykla.wordpress.com/2013-02-24/2013-02-24/
http://galvosukykla.wordpress.com/2013-02-25/2013-02-25/
http://galvosukykla.wordpress.com/2013-02-26/2013-02-26/
http://galvosukykla.wordpress.com/2013-02-27/2013-02-27/
http://galvosukykla.wordpress.com/2013-02-28/2013-02-28/
http://galvosukykla.wordpress.com/2013-03-01/2013-03-01/
http://galvosukykla.wordpress.com/2013-03-02/2013-03-02/
http://galvosukykla.wordpress.com/2013-03-03/2013-03-03/

