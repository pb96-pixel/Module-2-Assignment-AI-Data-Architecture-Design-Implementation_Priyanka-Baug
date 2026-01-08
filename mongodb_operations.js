Operation 1: Load Data (1 mark)
TASK: // Import the provided JSON file into collection 'products'

ANSWER:
// Operation 1: Load Data
// Import the provided JSON file into 'products' collection
// Command to be run in MongoDB shell:
//
// mongoimport --db fleximart --collection products --file products_catalog.json --jsonArray

---------------------------------------
Operation 2: Basic Query (2 marks)
TASK: // Find all products in "Electronics" category with price less than 50000
// Return only: name, price, stock

ANSWER:
// Operation 2: Basic Query
// Find all products in "Electronics" category with price less than 50000
// Return only name, price, and stock

db.products.find(
  { category: "Electronics", price: { $lt: 50000 } },
  { name: 1, price: 1, stock: 1, _id: 0 }
);

---------------------------------------
Operation 3: Review Analysis (2 marks)
TASK: // Find all products that have average rating >= 4.0
// Use aggregation to calculate average from reviews array

ANSWER:
// Operation 3: Review Analysis
// Find all products with average rating >= 4.0

db.products.aggregate([
  { $unwind: "$reviews" },
  {
    $group: {
      _id: "$name",
      avg_rating: { $avg: "$reviews.rating" }
    }
  },
  { $match: { avg_rating: { $gte: 4.0 } } }
]);

---------------------------------------
Operation 4: Update Operation (2 marks)
TASK: // Add a new review to product "ELEC001"
// Review: {user: "U999", rating: 4, comment: "Good value", date: ISODate()}

ANSWER:
// Operation 4: Update Operation
// Add a new review to product "ELEC001"

db.products.updateOne(
  { product_id: "ELEC001" },
  {
    $push: {
      reviews: {
        user: "U999",
        rating: 4,
        comment: "Good value",
        date: new Date()
      }
    }
  }
);

---------------------------------------
Operation 5: Complex Aggregation (3 marks)
TASK: // Calculate average price by category
// Return: category, avg_price, product_count
// Sort by avg_price descending

ANSWER:
// Operation 5: Complex Aggregation
// Calculate average price by category
// Return category, avg_price, product_count
// Sort by avg_price descending

db.products.aggregate([
  {
    $group: {
      _id: "$category",
      avg_price: { $avg: "$price" },
      product_count: { $sum: 1 }
    }
  },
  { $sort: { avg_price: -1 } }
]);