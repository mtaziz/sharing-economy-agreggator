<?php

class Dao_ProjectDao extends App_Model_Dao {

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

    public function get($projectId) {

        try{
            $query = Doctrine_Query::create()
                ->from('Model_CzProject p')
                ->where('p.id = ?',$projectId)
                ->orderBy('p.id DESC')
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getAll() {

        try{
            $query = Doctrine_Query::create()
                ->from('Model_CzProject p')
                ->orderBy('p.id DESC')
            ;

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getMyProjects($user_id,$type,$sousType,$project_id=null) {

        try{
            $query = Doctrine_Query::create()
                ->from('Model_CzProject p')
                ->Where('p.creator_id = ?',$user_id)
                ->orderBy('p.id DESC')
            ;
            if(!empty($type)){
                $query->andwhere('p.type = ?',$type);
            }
            if(!empty($sousType)){
                $query->andwhere('p.sousType = ?',$sousType);
            }
            if(!empty($project_id)){
                $query->andwhere('p.id = ?',$project_id);
            }

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

//TODO
    public function getProjectsByDepartment($departmentNumber) {

        try{
            $query = Doctrine_Query::create()
                ->from('Model_CzProject p')
                ->orderBy('p.id DESC')
                // ->innerJoin
            ;

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getProjectsByCity($postalCode) {

        try{
            $query = Doctrine_Query::create()
                
                ->from('Model_CzProject p')
                ->innerJoin('p.CzAddress a')
                ->Where('p.address_id = a.id')
                ->andWhere('a.zipcode like ?','%'.$postalCode)
                ->orderBy('p.id DESC')
            ;
            //  if(!empty($typeId)){
            //     $query->andwhere('c.company_type_id = ?',$typeId);
            // }

            return $query->execute();
            // return $query->execute(array(), Doctrine::HYDRATE_ARRAY);
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getProjectsByParams(array $params) {

        try{
            $query = Doctrine_Query::create()
                ->from('Model_CzProject p')
                ->orderBy('p.id DESC')
            ;

            if(!empty($params["postalCode"])){
                $query->innerJoin('p.CzAddress a')
                ->Where('p.address_id = a.id')
                ->andWhere('a.zipcode like ?','%'.$params["postalCode"]);
            } 

            if(!empty($params["type"]) && $params["type"]!="all"){
                $query->andwhere('p.type = ?',$params["type"]);
            }

            if(!empty($params["category_id"]) && $params["category_id"]!="all"){
                $query->innerJoin('p.CzProjectCategory pc')
                    ->andwhere('pc.project_id = p.id')
                    ->andwhere('pc.category_id = ?',$params["category_id"]);
            }

            return $query->execute();
            // return $query->execute(array(), Doctrine::HYDRATE_ARRAY);
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

}










        // try{
        //     $query = Doctrine_Query::create()
                
        //         ->from('Model_CzProject p')
        //         // ->select('c.id')
        //         ->innerJoin('p.CzAddress a')
        //         ->Where('a.zipcode = ?',$postalCode)
        //     ;
        //     // if(!empty($typeId)){
        //     //     $query->andwhere('c.company_type_id = ?',$typeId);
        //     // }

        //     return $query->execute(array(), Doctrine::HYDRATE_ARRAY);
        // }