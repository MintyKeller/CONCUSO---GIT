//A MongoDB Document
//Records in a MongoDB database are called documents, 
// and the field values may include numbers, strings, booleans, arrays, 
// or even nested documents.

use('meu_teste');
db.testing.insertOne({
	title: "Post Title 1",
	body: "Body of post.",
	category: "News",
	likes: 1,
	tags: ["news", "events"],
	date: Date()
}); 

db.posts.find( {category: "News"} )

/*
SQL vs Document Databases

SQL databases are considered relational databases. 
They store related data in separate tables. 
When data is needed, it is queried from multiple tables to join the data back together.

MongoDB is a document database which is often referred to as a non-relational database.
 This does not mean that relational data cannot be stored in document databases. 
 It means that relational data is stored differently. 
 A better way to refer to it is as a non-tabular database.

MongoDB stores data in flexible documents. 
Instead of having multiple tables you can simply keep all of your related data together. 
This makes reading your data very fast.

You can still have multiple groups of data too. 
In MongoDB, instead of tables these are called collections.
*/

//CREATING DATABASE 
//use databese
//Remember: In MongoDB, a database is not actually created until it gets content!

//MongoDB mongosh Create Collection
db.createCollection("posts");
//You can also create a collection during the insert process.
db.posts.insertOne(object); //We are here assuming object is a valid JavaScript object containing post data:

//Remember: In MongoDB, a collection is not actually created until it gets content!

//MongoDB mongosh Insert

/*
Insert Documents
There are 2 methods to insert documents into a MongoDB database.
insertOne() AAAAND insertMany()
*/

//To insert a single document, use the insertOne() method.
db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date()
}); 

//Note: If you try to insert documents into a collection that does not exist,
//  MongoDB will create the collection automatically.

//To insert multiple documents at once, use the insertMany() method.
//This method inserts an array of objects into the database.

db.posts.insertMany([  
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date()
  }
]);

//MongoDB mongosh Find
    //Find Data
    //There are 2 methods to find and select data from a MongoDB collection, find() and findOne().

    /*
     find()
To select data from a collection in MongoDB, we can use the find() method.

This method accepts a query object. If left empty, all documents will be returned.
     */

db.posts.find();

    /*findOne()
To select only one document, we can use the findOne() method.

This method accepts a query object. 
If left empty, it will return the first document it finds.

Note: This method only returns the first match it finds.*/
db.posts.findOne(); 

    /* Querying Data
To query, or filter, data we can include a query in our find() or findOne() methods.
    */
db.posts.find( {category: "News"} ); 

    /* Projection
Both find methods accept a second parameter called projection.

This parameter is an object that describes which fields to include in the results.

Note: This parameter is optional. If omitted, all fields will be included in the results.

This example will only display the title and date fields in the results.*/
db.posts.find({}, {title: 1, date: 1})

//We use a 1 to include a field and 0 to exclude a field.
db.posts.find({}, {_id: 0, title: 1, date: 1})

    /*Note: You cannot use both 0 and 1 in the same object. 
    The only exception is the _id field. You should either specify 
    the fields you would like to include or the fields you would like to exclude.
 */
db.posts.find({}, {category: 0})

//this is gonna get you an error
//db.posts.find({}, {title: 1, date: 0})

//MongoDB mongosh Update

    /*Update Document
To update an existing document we can use the updateOne() or updateMany() methods.

The first parameter is a query object to define which document or documents should be updated.

The second parameter is an object defining the updated data.*/

    /*updateOne()
The updateOne() method will update the first document that is found matching the provided query. */
db.posts.updateOne( { title: "Post Title 1" }, { $set: { likes: 2 } } ) ; //it needs to use the $set operator

//inserting if not found: Update the document, but if not found insert it:

db.posts.updateOne( 
  { title: "Post Title 5" }, 
  {
    $set: 
      {
        title: "Post Title 5",
        body: "Body of post.",
        category: "Event",
        likes: 5,
        tags: ["news", "events"],
        date: Date()
      }
  }, 
  { upsert: true } //If you would like to insert the document if it is not found, you can use the upsert option.
); 

/*
updateMany()
The updateMany() method will update all documents that match the provided query.*/
//Update likes on all documents by 1. For this we will use the $inc (increment) operator:
db.posts.updateMany({}, { $inc: { likes: 1 } }); 

//MongoDB mongosh Delete

    /*Delete Documents
We can delete documents by using the methods deleteOne() or deleteMany().

These methods accept a query object. The matching documents will be deleted.*/

    /*deleteOne()
The deleteOne() method will delete the first document that matches the query provided. */
db.posts.deleteOne({ title: "Post Title 5" }); 

    /*deleteMany()
The deleteMany() method will delete all documents that match the query provided.
 */
db.posts.deleteMany({ category: "Technology" })

    /*MongoDB Query Operators*/
    //There are many query operators that can be used to compare and reference document fields.

    /*
    Comparison
The following operators can be used in queries to compare values:

$eq: Values are equal
$ne: Values are not equal
$gt: Value is greater than another value
$gte: Value is greater than or equal to another value
$lt: Value is less than another value
$lte: Value is less than or equal to another value
$in: Value is matched within an array

    Logical
The following operators can logically compare multiple queries.

$and: Returns documents where both queries match
$or: Returns documents where either query matches
$nor: Returns documents where both queries fail to match
$not: Returns documents where the query does not match

    Evaluation
The following operators assist in evaluating documents.

$regex: Allows the use of regular expressions when evaluating field values
$text: Performs a text search
$where: Uses a JavaScript expression to match documents
     */
    
//MongoDB Update Operators

    /*MongoDB Update Operators
There are many update operators that can be used during document updates.

    Fields
The following operators can be used to update fields:

$currentDate: Sets the field value to the current date
$inc: Increments the field value
$rename: Renames the field
$set: Sets the value of a field
$unset: Removes the field from the document

    Array
The following operators assist with updating arrays.

$addToSet: Adds distinct elements to an array
$pop: Removes the first or last element of an array
$pull: Removes all elements from an array that match the query
$push: Adds an element to an array */

//MongoDB Aggregation Pipelines
    /*Aggregation Pipelines
Aggregation operations allow you to group, sort, perform calculations, 
analyze data, and much more.

Aggregation pipelines can have one or more "stages". The order of these stages are important. 
Each stage acts upon the results of the previous stage. */

db.posts.aggregate([
  // Stage 1: Only find documents that have more than 1 like
  {
    $match: { likes: { $gt: 1 } }
  },
  // Stage 2: Group documents by category and sum each categories likes
  {
    $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
  }
]); 


use("bd_spot_file");
/*Aggregation $group
This aggregation stage groups documents by the unique _id expression provided. 
(THE ID IS THE CRITERIA), Don't confuse this _id expression with the _id ObjectId provided to each document.
*/
db.albuns.aggregate([
  { $group: { _id: "$id_artista", total_albuns: { $sum: 1 } } }
]);
/*
Aggregation $limit
This aggregation stage limits the number of documents passed to the next stage.
*/
db.albuns.aggregate([
  { $limit: 3 }
]);
/*
Aggregation $project
This aggregation stage passes only the specified fields along to the next aggregation stage.

This is the same projection that is used with the find() method.
*/
db.albuns.aggregate([
  { $project: { _id: 0, nome: 1, ano_lancamento: 1 } }
]);

/*
Aggregation $sort
This aggregation stage groups sorts all documents in the specified sort order.

Remember that the order of your stages matters. Each stage only acts upon the documents that previous stages provide.
*/
db.albuns.aggregate([
  { $sort: { ano_lancamento: 1 } }
]);
/*
Aggregation $match
This aggregation stage behaves like a find. It will filter documents that match the query provided.

Using $match early in the pipeline can improve performance since it limits the number of documents the next stages must process.
*/
db.albuns.aggregate([
  { $match: { ano_lancamento: 2000 } }
]);
/*
Aggregation $addFields
This aggregation stage adds new fields to documents.
*/
db.albuns.aggregate([
  { $addFields: { status: "arquivado" } }
]);
/*
Aggregation $count
This aggregation stage counts the total amount of documents passed from the previous stage.
*/
db.albuns.aggregate([
  { $count: "total_geral" }
]);
/*
Aggregation $lookup
This aggregation stage performs a left outer join to a collection in the same database.

There are four required fields:

from: The collection to use for lookup in the same database
localField: The field in the primary collection that can be used as a unique identifier in the from collection.
foreignField: The field in the from collection that can be used as a unique identifier in the primary collection.
as: The name of the new field that will contain the matching documents from the from collection.
*/
db.albuns.aggregate([
  {
    $lookup: {
      from: "artistas",
      localField: "id_artista",
      foreignField: "_id",
      as: "detalhes_do_artista"
    }
  }
]);
/*
Aggregation $out
This aggregation stage writes the returned documents from the aggregation pipeline to a collection.

The $out stage must be the last stage of the aggregation pipeline.

The first stage will group properties by the property_type and include the name, accommodates, and price fields for each. The $out stage will create a new collection called properties_by_type in the current database and write the resulting documents into that collection.
*/

db.albuns.aggregate([
  { $match: { ano_lancamento: 1991 } },
  { $out: "albuns_de_1991" }
]);