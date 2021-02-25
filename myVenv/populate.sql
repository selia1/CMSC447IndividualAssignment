/*****************************************************************
 * File: populate.sql
 * Author: Sean Elia
 * Project: CMSC 447 Individual Assignment 1, Spring 2021
 *
 * An SQL script to fill the database with the initial data
*****************************************************************/

-- Empties any data stored in StudentTable
DELETE FROM StudentTable;

-- Fills StudentTable with the initial data
INSERT INTO StudentTable
VALUES
    (21, "Joe", 90), 
    (22, "Jain", 92), 
    (23, "Chris", 90), 
    (24, "Sai", 95),
    (25, "Andrew", 100),
    (26, "Lynn", 90),
    (27, "Robert", 85);

