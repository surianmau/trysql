from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
import psycopg2


@api_view(['GET'])
def apitry(request):
    franchiseId = request.GET.get('franchiseId')
    print(franchiseId,"franchiseId")
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "jasmine123",
                                      host = "3.19.56.83",
                                      port = "5432",
                                      database = "grocsosv1")
        # Print PostgreSQL Connection properties


        cursor = connection.cursor()

        create_table_query = '''select franchiseid, id as storeid, storecode,name as storeName,chainName,image as storeImage, description as shortDesc
	from Store WHERE franchiseid = %s'''

        cursor.execute(create_table_query,(franchiseId,))
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