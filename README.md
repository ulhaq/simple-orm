# Simple ORM
Specifications of the entities:
```json
{"schemaName": "MicroShop",
  "entities": [
  	{"Customer": {
  		"name": "String",
  		"orders" :"*Order"}},
  	{"Order" :{
  		"date": "String",
  		"total": "Number",
  		"customer": "Customer",
  		"lines": "*OrderLine" }},
  	{"OrderLine" : {
  		"order": "Order",
  		"product": "Product",
  		"count": "Number",
  		"total": "Number" }},
  	{"Product" : {
  		"name": "String",
  		"price" :"Number"}}
  ]
}
```