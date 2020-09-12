from rest_framework.decorators import api_view
from rest_framework.response import Response
import psycopg2


@api_view(['GET'])
def storeandcategory(request):
    storeID = request.GET.get('storeid')
    categoryid =  request.GET.get('productCategoryId')
    print(storeID,"storeID")
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "jasmine123",
                                      host = "3.23.172.82",
                                      port = "5432",
                                      database = "grocsosv1")

        cursor = connection.cursor()

        create_table_query = '''SELECT distinct  P.ID, P.name as productName,
			t.categoryid1 as ProductCategoryId1, c.Name as ProductCategoryName1,
			t.categoryid2 as ProductCategoryId2, c1.Name as ProductCategoryName2 ,
	 		i.unit,
			i.variants,
			p.msrp,
			i.price as unitPrice,
			p.image as productImage
	 from Inventory i
	 inner join Product p on (p.id =i.productid) 
	 inner join productcategorytree t on (t.categoryid= p.categoryid)
	 inner join productcategory c on (c.id = t.categoryid1)
	 left outer join productcategory c1 on (c1.id = t.categoryid2)
	where i.storeid = %s and categoryid1 = 1 and categoryid2 =  %s  order by p.name'''

        cursor.execute(create_table_query,(storeID,categoryid,))
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
        return Response('bye')