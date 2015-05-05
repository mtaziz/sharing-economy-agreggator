<?php

class Dao_LanguageDao extends App_Model_Dao {

    public function getLanguage($id) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Language l')
                ->where('l.id = ?',$id)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getLanguageByType($type) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Language l')
                ->where('l.type = ?',$type)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getLanguages() {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Language l')
            ;

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
}