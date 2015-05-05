<?php

class Dao_CzOrganisationDao extends App_Model_Dao {

    public function save($model) {

        try{

            $model->save();
            return true;
        }
        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function delete($model) {

        try{

            $model->delete();
            return true;
        }
        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
        
    public function getCity($id) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Organization c')
                ->where('c.orga_id = ?',$id)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    public function getCityByName($name) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Organization c')
                ->where('c.domain = ?',$name)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getOrgaByPostalcode($cp) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Organization c')
                // ->where('c.listPostalCode like ?',"%".$cp."%")
                ->where('c.listPostalCode like ?','%,'.$cp.',%')
            ;

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getAllCities() {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Organization c')
                ->where('c.domain != "null"')
                ->andwhere('c.domain != ""')
                ->andwhere('c.title != ""')
            ;

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

}