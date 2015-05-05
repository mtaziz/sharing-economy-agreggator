<?php

class Admin_Dao_AdDao extends App_Model_Dao {

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

    public function searchAd($search, $page = 1) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Ad a');

            // Filters
            if (isset($search['words']) && !empty($search['words']) && count($search['words']) > 0) {
                foreach ($search['words'] as $word) {
                    $query->andWhere('a.title LIKE ?','%'.$word.'%');
                }
            }
            if (isset($search['company_id']) && $search['company_id'] > 0) {
                $query->innerJoin('a.User u')
                    ->innerJoin('u.UserCompany uc')
                    ->andWhere('uc.company_id = ?',$search['company_id']);
            }
            if (isset($search['state']) && strlen($search['state']) > 0) {
                $query->andWhere('a.state = ?',$search['state']);
            }
            if (isset($search['user_id']) && $search['user_id'] > 0) {
                $query->innerJoin('a.User u2')
                    ->andWhere('u2.id = ?',$search['user_id']);
            }
            if (isset($search['category_id']) && $search['category_id'] > 0) {
                $query->innerJoin('a.Category c')
                    ->andWhere('c.id = ?',$search['category_id']);
            }
            // --

            $query->orderBy('a.created_at DESC')
            ;

            $paginator = new Zend_Paginator(new App_Paginator_Adapter_Doctrine($query));
            $paginator->setItemCountPerPage(25)
                ->setCurrentPageNumber($page);

            return $paginator;
            //return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function nbAdsByDay($dateDebut=null, $dateFin=null){
        
        try{
            $con = Doctrine_Manager::getInstance()->connection();
            if($dateDebut != null && $dateFin != null){ 
                $between = "WHERE created_at BETWEEN '".$dateDebut."' And '".$dateFin."' ";
            } else{ 
                $between = "";
            }

            $st = $con->execute("SELECT created_at, COUNT( created_at ) 
            FROM ad
            ".$between."
            GROUP BY YEAR(created_at) ,MONTH( created_at ) , DAY( created_at )");

            return $st->fetchAll();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getMedia($id) {
		
		try{
	
			$query = Doctrine_Query::create()
			->from('Model_Media m')
			->where('m.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
  	
    public function getAd($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Ad a')
			->where('a.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

   	public function getAdbyState($state=null, $page=1, $intervalDate=null){
//anis 20/02/2014__________________________________________________________________________
        try{

            $query = Doctrine_Query::create()
            ->from('Model_Ad a');

            if (isset($state)) {
                $query->Where('a.state IN ('.$state.')');
            }
            
            if(isset($intervalDate)){

                // $query->andWhere("a.created_at BETWEEN NOW() AND :interval");
                // $now = new Zend_Date::now();
                // $datemax= $now->sub($intervalDate, Zend_Date::DAY);
                // $query->andWhere('created_at >= ';
                // ->setParameter('interval', "NOW()-INTERVAL '".$intervalDate."' DAY")

                // $D2 = "NOW()+INTERVAL ".$intervalDate." DAY"


//__REQUETES SQL______________________________________
//____________________________________________________
// SELECT *
// FROM ad
// WHERE created_at 
// BETWEEN 
// NOW() 
// AND 
// DATE_ADD(NOW() , INTERVAL 100 DAY)
//____________________________________________________
// SELECT *
// FROM ad
// WHERE created_at 
// BETWEEN                                            
// adddate(-7,now() ) and now()
//____________________________________________________

            }

            $query->orderBy('a.id DESC');

            $paginator = new Zend_Paginator(new App_Paginator_Adapter_Doctrine($query));
            $paginator->setItemCountPerPage(25)
                ->setCurrentPageNumber($page);

            return $paginator;
            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
//_________________________________________________________________________________________
   	}

    public function countRegisteredAds() {
//anis 03/03/2014
        try{

            $query = Doctrine_Query::create()
                ->from('Model_Ad c')
                ->where('c.state = ?','available')
                ->orderBy('c.id DESC')
            ;

            return $query->count();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    
    public function getAdsWithState($state) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Ad a')
			->where('a.state = ?',$state)
			->limit(10)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getAdFieldDefault($id, $lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_AdFieldDefault afd')
			->innerJoin('afd.TranslateAdFieldDefault t')
			->where('afd.id = ?',$id)
			->andWhere('t.language_id = ?',$lang)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getAdFieldsDefault($lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_AdFieldDefault afd')
			->innerJoin('afd.TranslateAdFieldDefault t ON afd.id = ad_field_default_id AND t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getAdFieldsDefaultArray($lang = BO_LANG) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_AdFieldDefault afd')
                ->innerJoin('afd.TranslateAdFieldDefault t ON afd.id = ad_field_default_id AND t.language_id = ?',$lang)
            ;

            return $query->fetchArray();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function deleteTranslations($lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->delete('Model_TranslateAdFieldDefault t')
			->where('t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}