<?php

class Dao_DatasDao extends App_Model_Dao {

    // public function save($model) {

    //     try{

    //         $model->save();
    //         return true;
    //     }
    //     catch(Exception $e){
    //         throw new App_Exception_Model($e->getMessage());
    //     }
    // }

    // public function delete($model) {

    //     try{

    //         $model->delete();
    //         return true;
    //     }
    //     catch(Exception $e){
    //         throw new App_Exception_Model($e->getMessage());
    //     }
    // }

    public function getAll($source=null) {

        // bootstrap.php
// $dsn = 'mysql:dbname=matthieuhdatas;host=matthieuhdatas.mysql.db';
// $user = 'matthieuhdatas';
// $password = '59G5stKEu8';

// $dbh = new PDO($dsn, $user, $password);
// $conn = Doctrine_Manager::connection($dbh);


        // $parameters = array(
        //             'host'     => 'matthieuhalterr.mysql.db',
        //             'username' => 'matthieuhalterr',
        //             'password' => 'vQ524F8xdR',
        //             'dbname'   => 'matthieuhalterr'
        //                    );
        // try {
        //     $db = Zend_Db::factory('Pdo_Mysql', $parameters);
        //     $db->getConnection();
        // } catch (Zend_Db_Adapter_Exception $e) {
        //     echo $e->getMessage();
        //     die('Could not connect to database.');
        // } catch (Zend_Exception $e) {
        //     echo $e->getMessage();
        //     die('Could not connect to database.');
        // }
        // Zend_Registry::set('db', $db);

        // $config = Zend_Registry::get('config');
        // $dsn2=$config->resources->doctrine->dsn2; 

        // try{
            // $con = Doctrine_Manager::getInstance()->connection();
             // Connexion à la bdd de stockage
            // $conn = Doctrine_Manager::connection('mysql://matthieuhdatas:59G5stKEu8@matthieuhdatas.mysql.db/matthieuhdatas');
            // $conn = Doctrine_Manager::getInstance()->connection('mysql://matthieuhalterr:vQ524F8xdR@matthieuhalterr.mysql.db/matthieuhalterr');
           // $conn = Doctrine_Manager::getInstance()->connection();
           // $conn1 = Doctrine_Manager::connection('mysql://matthieuhalterr:vQ524F8xdR@matthieuhalterr.mysql.db/matthieuhalterr','doctrine');
           // Zend_Registry::set('conn1',$conn1);
           // $conn2 = Doctrine_Manager::connection('mysql://matthieuhdatas:59G5stKEu8@matthieuhdatas.mysql.db/matthieuhdatas','doctrine_data');
           // Zend_Registry::set('conn2',$conn2);
           // // $conn2 = Doctrine_Manager::connection('mysql://matthieuhdatas:59G5stKEu8@matthieuhdatas.mysql.db/matthieuhdatas');
           // // Zend_Registry::set('conn2',$conn2);

           // $conn = Zend_Registry::get('conn1');
           // // $conn = Zend_Registry::get('conn2');
           //  $st = $conn->execute("SELECT * FROM `user`");
           //  // $st = $conn->execute("SELECT * FROM `ads`");
           //  // $st= $conn2->execute('SHOW TABLES');
           //  //$st = $conn->execute("SELECT * FROM `ads` WHERE source='".$source."'");

           //  // return $st;
           //  return $st->fetchAll();
        // }

        // catch(Exception $e){
            // throw new App_Exception_Model($e->getMessage());
        // }
   }     
}