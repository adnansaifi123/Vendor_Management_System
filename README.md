# Vendor_Management_System

This project aims to develop a Vendor Management System (VMS) using Django and Django REST Framework. The system will facilitate the management of vendor profiles, tracking of purchase orders, and calculation of vendor performance metrics.
Installation

Create and activate a virtual environment:

``` 
python -m venv venv
.\venv\Scripts\activate
```
Install dependencies:
`` pip install -r requirements.txt``

Run migrations:
````
python manage.py makemigrations
python manage.py migrate
````

Run
``python manage.py runserver`` to start the server



## Features
### Vendor Profile Management:
APIEndpoints:
 ````
 ● POST/api/vendors/: Create a new vendor.
 ● GET/api/vendors/: List all vendors.
 ● GET/api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
 ● PUT/api/vendors/{vendor_id}/: Update a vendor's details.
 ● DELETE/api/vendors/{vendor_id}/: Delete a vendor.
 ````

#### 1. ``POST/api/vendors/: Create a new vendor.``

Sample JSON for Creating a New Vendor
````
{
    "name": "Vendor2",
    "contact_details": "123-456-7890",
    "address": "1111 Main St, City",
    "vendor_code": "SAMPLE002"
}
````

![img_2](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/8aa9b25a-e56e-4ce5-adfa-b92a7f99c4c8)

#### 2.  ``GET/api/vendors/: List all vendors.``
![img_4](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/9dff9ee7-b952-4e60-9bfe-c5e3393439ef)


#### 3. ``GET/api/vendors/{vendor_id}/: Retrieve a specific vendor's details.``
![img_5](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/1d83bc92-05f0-44b6-a311-04fb66b8e154)



#### 4. ``PUT/api/vendors/{vendor_id}/: Update a vendor's details.``
![img_6](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/08bfafd5-7983-41a8-854f-a2c2e0a23a9f)



#### 5. ``DELETE/api/vendors/{vendor_id}/: Delete a vendor.``
![img_7](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/750f0028-ab31-4482-81ce-625665d44f0e)



### Purchase Order Tracking:
APIEndpoints:
````
 ● POST/api/purchase_orders/: Create a purchase order.
 ● GET/api/purchase_orders/: List all purchase orders with an option to filter by
 vendor.
 ● GET/api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
 ● PUT/api/purchase_orders/{po_id}/: Update a purchase order.
 ● DELETE/api/purchase_orders/{po_id}/: Delete a purchase order.
````

#### 1. ``POST/api/purchase_orders/: Create a purchase order.``
Sample JSON for Creating a Purchase Order
````
{
    "po_number": "PO002",
    "vendor": "SAMPLE002",
    "order_date": "2024-05-10T10:00:00",
    "delivery_date": "2024-06-20T10:00:00",
    "items": [{"name": "Item1", "quantity": 5},{"name": "Item2", "quantity": 10}],
    "quantity": 10,
    "status": "pending"
}
````
![img_14](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/26ba4e6d-99b1-4d09-9113-3eaac4c14275)


#### 2 ``GET/api/purchase_orders/: List all purchase orders with an option to filter by  vendor``
![img_9](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/9112d68b-cbe4-48b1-b893-390ba238b6ec)



#### 3 ``GET/api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.``
![img_10](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/76aedb05-c562-4f5e-b71e-faa6bb943005)

#### 4 ``PUT/api/purchase_orders/{po_id}/: Update a purchase order``
![img_11](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/b4584ae3-f3e6-4c45-a2bf-ce37abb6c908)

Note: In this Vendor Management System, the performance metrics for vendors are recalculated whenever the status of a purchase order changes. This dynamic update ensures that metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate are always up-to-date based on the latest data. 
This approach to recalculating metrics ensures that our performance evaluations are accurate and reflect the current status of vendor performance.![img_12](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/7ed8cd83-426a-49aa-8db5-8bb155370bd3)


#### 5 ``DELETE/api/purchase_orders/{po_id}/: Delete a purchase order.``
![img_13](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/bc8b0b0b-4a7f-4619-9df5-0b42a423821f)


#### 6 ``POST/api/purchase_orders/{po_id}/acknowledge : Update Acknowledgement Date``
![img_15](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/adc49521-2da6-46aa-b8e3-2ae21c0eb513)

### Vendor Performance Evaluation
````
 APIEndpoints:
 ● GET/api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
 metrics
````
![img_16](https://github.com/adnansaifi123/Vendor_Management_System/assets/67619920/23c8d107-c53e-432a-802d-eda5334bc9af)
