<?php

class Dao_AdsDao extends App_Model_Dao {

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

    public function getAll($page,$filters = array()) {

      try{

        if (isset($filters['rayon'])) {
            $radius=$filters['rayon'] / (60 * 1.852);
        }else{
            $radius=30;
            $radius = $radius / (60 * 1.852);
        }
      
        // $words = array();
        // if (isset($filters['words'])) {
        //     $words = explode(' ',$filters['words']);
        // }

        $query = Doctrine_Query::create()
        ->from('Model_Ads a');

        if (isset($filters['category']) && !empty($filters['category']) && $filters['category'] != 'all') {
             $query->andwhere('a.category = ?',$filters['category']);
            //Explode de l'array
            // $stringCat=str_replace("-", ",", mysql_escape_string($filters['category']));
            // $query->andWhere('a.category_id IN ('.$stringCat.')');
        }

        if (isset($filters['subcategory']) && !empty($filters['subcategory']) && $filters['subcategory'] != 'all') {
             $query->andwhere('a.subcategory = ?',$filters['subcategory']);
        }

        $query->andWhere("a.title LIKE ? OR a.title LIKE ? OR a.description LIKE ? OR a.description LIKE ?",array('%'.$filters['words'],$filters['words'].'%','%'.$filters['words'],$filters['words'].'%'));  

        // if (count($words) > 0) {

            // $req = '';
            // $req2 = '';
            // $cpt = 1;
            // $wordArray = array();
            // foreach($words as $word) {
                
            //     $wordArray[] = '%'.$word.'%';   
            //     $req .= 'a.title LIKE ?';                       
            //     // $req2 .= 'a.description LIKE ?';                       
            //     if ($cpt < count($words)) {
            //         $req .= ' OR ';
            //         // $req2 .= ' OR ';
            //     }
            //     $cpt++;
            // }
            
            
            // $query->orWhere("a.description LIKE ?",'%'.$filters['words'].'%');
            // $query->andWhere($req,$wordArray);
            // $query->andWhere($req2,$wordArray);
        // }


        if (isset($filters['address_lat']) && !empty($filters['address_lat']) && isset($filters['address_lng']) && !empty($filters['address_lng'])) {
             $query->andwhere(
                "SQRT(POW((a.latitude - ".$filters['address_lat']."), 2) + POW((a.longitude - ".$filters['address_lng']."),2)) < ".$radius
                 // $filters['address_lat']."!='unknown' AND ".$filters['address_lng']."!='unknown' AND SQRT(POW((a.latitude - ".$filters['address_lat']."), 2) + POW((a.longitude - ".$filters['lng']."),2)) < ".$radius
                );

        }else{
            // geocoding inverse de l'adresse pour récupérer les lat/lng
            
        }

        $paginator = new Zend_Paginator(new App_Paginator_Adapter_Doctrine($query));
            $paginator->setItemCountPerPage(25)
                ->setCurrentPageNumber($page);

            return $paginator;
    }
    
    catch(Exception $e){
      throw new App_Exception_Model($e->getMessage());
    }

   }     
}