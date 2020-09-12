from rest_framework.decorators import api_view
from rest_framework.response import Response
import psycopg2

@api_view(['GET'])
def findbystore(request):
    storeid = request.GET.get("storeid")
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "jasmine123",
                                      host = "3.23.172.82",
                                      port = "5432",
                                      database = "grocsosv1")
        cursor = connection.cursor()
        create_table_query = '''SELECT distinct t.categoryid1 as Id, c.name categoryName, c.image as categoryImage,
	(select 1  where exists ( 
			select * from productcategorytree t1 
			where t.categoryid1 = t1.categoryid1 
			and t1.categoryid2 is not null)
	)   as "Subcategory Exists"
	 from Inventory i
	 inner join Product p on (p.id =i.productid) 
	 inner join productcategorytree t on (t.categoryid= p.categoryid)
	 inner join productcategory c on (c.id = t.categoryid1)
	 where i.storeid = %s order by c.name'''

        cursor.execute(create_table_query,(storeid,))
        rows = cursor.fetchall()
        a= []
        for i in rows:
            a.append(i)
        connection.commit()
        print(" output came successfully ")
        cursor.close()
        connection.close()
        return Response(a)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        return Response("e")