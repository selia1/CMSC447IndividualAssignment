/*****************************************************************
 * File: populate.sql
 * Author: Sean Elia
 * Project: CMSC 447 Individual Assignment 1, Spring 2021
 *
 * An SQL script to create the database used for this assignment
*****************************************************************/

-- Creates a named Student Table
CREATE TABLE IF NOT EXISTS StudentTable
(   studentId int,
    studentName varchar(256),
    studentMarks int,
    PRIMARY KEY (id)
);

