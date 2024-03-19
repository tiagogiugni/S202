from database import Database

class ProductAnalyzer:
    def __init__(self, database: Database):
        self.db = database.collection

    def total_sales_per_day(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$data_compra",
                "totalVendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"_id": 1}}
        ]
        return list(self.db.aggregate(pipeline))

    def most_sold_product(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "totalQuantidade": {"$sum": "$produtos.quantidade"}
            }},
            {"$sort": {"totalQuantidade": -1}},
            {"$limit": 1}
        ]
        return list(self.db.aggregate(pipeline))

    def top_spender_customer(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$cliente_id",
                "totalGasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"totalGasto": -1}},
            {"$limit": 1}
        ]
        return list(self.db.aggregate(pipeline))

    def products_sold_above_one(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "totalQuantidade": {"$sum": "$produtos.quantidade"}
            }},
            {"$match": {"totalQuantidade": {"$gt": 1}}}
        ]
        return list(self.db.aggregate(pipeline))