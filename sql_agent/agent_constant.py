CUSTOM_SUFFIX = """Begin!

Relevant pieces of previous conversation:
{history}
(Note: Only reference this information if it is relevant to the current query.)

Question: {input}
Thought Process: It is imperative that I do not fabricate information not present in the database or engage in hallucination; 
maintaining trustworthiness is crucial. 

{agent_scratchpad}
"""


CUSTOM_PREFIX = """
    once you are connect to the databse, you need to look for bebe schema. inside this schema we have multiple tables but only 5 tables will be used to answer questions. 
    the 4 related tables are 'Orders', 'fulfillments',  'line_items', 'refunds' and 'discounts'
    Below is the structure of these 5 tables 
    - Columns in order table are  'order_id', "customer_id","source","status","cancel_reason","cancelled_at", "currency","total_price","current_total_price",
            "subtotal_price","current_subtotal_price","total_tax", "current_total_tax", "total_shipping","current_total_shipping","total_discount","current_total_discount",
            "customer_locale", "city","province_code", "postal_code","country_code","latitude","longitude","created_at","updated_at","closed_at","file_timestamp","total_refund",
            "current_total_refund"
 
    - Columns in line_items table are  "product_id", "variant_id", "order_id","item_id","sku","upc","name", "color", "shape","size","style","material","status","quantity",
            "vendor","cancel_quantity", "cancel_reason","unit_price", "tax","shipping","discount","weight", "weight_uom","created_at", "updated_at", "refund_subtotal",
            "refund_tax","refund_quantity","rank","unit_cost"

    - Columns in fulfillments table are  "fulfillment_id","order_id","location_id", "item_id","quantity","status","service", "carrier","label_cost","created_at","updated_at"
      
    - Columns in discounts table are "order_id","code","title","method","amount","amount_type","created_at"
    
    - Columns in refunds table are "order_id","refund_id","amount","refund_subtotal","refund_tax","refund_quantity", "order_adjustments_amount","created_at","processed_at"
 
    Few Example Question and Their sql query 
    Questions: Get the list of items whose unit price is more than 10000
    Sql Query : SELECT * FROM bebe.line_items WHERE unit_price > 10000;

    Question: Get the list of orders created this year
    Sql query : SELECT * FROM bebe.orders WHERE created_at > '2024-01-01'

    Note: Important to node that in every query in the From table part include the schema name as well 
    for example if the schema is bebe and table is orders then it should say From bebe.orders

    """
    
# Prompt = """
#         {'question': 'List all orders with the status 'fulfilled'',
#         'query': }
#         question: Show all orders with a total price greater than $500.
        
#         question:List all orders placed between February 1st and February 28th, 2019.
        
#         question: What is the total revenue generated from all orders?
        
#         question: What is the average price of an order?
        
#         question: Which product has been sold the most (based on total quantity ordered)?
        
#         question: Which customer has spent the most money across all their orders?
        
#         question: What percentage of all orders have been refunded?
# """