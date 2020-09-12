from rest_framework.decorators import api_view
from rest_framework.response import Response
import psycopg2
import datetime
@api_view(['POST'])
def insertorders(request):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "jasmine123",
                                      host = "3.23.172.82",
                                      port = "5432",
                                      database = "grocsosv1")
        cursor = connection.cursor()
        now = datetime.date.today()
        CustomerId = 9,
        shippingaddressid = request.POST.get('shippingaddressid')
        storeid = request.POST.get('storeid')
        deliverywindowid = request.POST.get('deliverywindowid')
        pickupwindowid = request.POST.get('pickupwindowid')
        totalamount = request.POST.get('totalamount')
        createdby = 'velur',
        create_table_query = '''insert into orders(date,status,userid,shippingaddressid,storeid,deliverywindowid,pickupwindowid,
        				  totalamount,createdby) 
        			values(%s,'Ordered', %s, %s,%s, null, %s, %s, %s) returning id'''
        cursor.execute(create_table_query,
                       (now, CustomerId, shippingaddressid, storeid, pickupwindowid, totalamount, createdby))
        cursor1 = connection.cursor()
        oderid = request.POST.get('oderid'),
        productid = request.POST.get('productid')
        quantity = request.POST.get('quantity')
        unitprice = request.POST.get('unitprice')
        createdby = 'velur',
        totalamount1 = request.POST.get('totalamount1')
        create_table_query = '''insert into orderitemsmap(orderid, productid, quantity, unitprice, totalamount, createdby )
        			values(%s, %s, %s,%s ,%s ,%s )'''
        cursor1.execute(create_table_query, (oderid, productid, quantity, unitprice, totalamount1, createdby,))
        connection.commit()
        print(" output came successfully ")
        cursor.close()
        cursor1.close()
        connection.close()
        return Response("hi")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        return Response('bye')