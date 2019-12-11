//package com.snhu.app;

import com.mongodb.BasicDBObject;
import com.mongodb.BulkWriteOperation;
import com.mongodb.BulkWriteResult;
import com.mongodb.Cursor;
import com.mongodb.DB;
import com.mongodb.DBCollection;

import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;
import com.mongodb.ParallelScanOptions;
import com.mongodb.ServerAddress;
import java.util.List;
import java.util.Set;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.ClassNotFoundException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

import static java.util.concurrent.TimeUnit.SECONDS;

public class App {
  
  /* C from CRUD functions for creating a document */
  public static void create_document(BasicDBObject doc) {
    try {
      MongoClient mg = new MongoClient("localhost");
      DB db = mongoClient.getDB("market");
      DBCollection coll = db.getCollection("stocks");
      coll.insert(doc);
    } catch (UnknownHostException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
  
  public static void read_document(BasicDBObject doc) {
    try {
      MongoClient mg = new MongoClient("localhost");
      DB db = mongoClient.getDB("market");
      DBCollection coll = db.getCollection("stocks");
      coll.insert(doc);
    } catch (UnknownHostException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
  
  public static void main (String[] args) {
    
    BasicDBObject doc = new BasicDBObject("Ticker", "DNZ");
    
    create_document(doc);
  }
}