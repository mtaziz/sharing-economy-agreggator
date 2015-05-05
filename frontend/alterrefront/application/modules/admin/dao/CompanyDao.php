<?php

class Admin_Dao_CompanyDao extends App_Model_Dao {

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
    
    public function getCompany($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Company c')
			->where('c.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getCompanies($state=null, $page = 1) {

        try{

            $query = Doctrine_Query::create()
            ->from('Model_Company c');

            if (isset($state)) {
                $query->where('c.state IN ('.$state.')');
            }

            $query->orderBy('c.id DESC');

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

    public function getRegisteredCompanies($page = 1) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Company c')
                ->where('c.state = ?','registered')
                ->orderBy('c.id DESC')
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

    public function countRegisteredCompanies() {
//anis 03/03/2014
        try{

            $query = Doctrine_Query::create()
                ->from('Model_Company c')
                ->where('c.state = ?','registered')
                ->orderBy('c.id DESC')
            ;

            return $query->count();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function searchCompanies($search, $page = 1) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Company c');

            // Filters
            if (isset($search['words']) && !empty($search['words']) && count($search['words']) > 0) {
                foreach ($search['words'] as $word) {
                    $query->andWhere('c.name LIKE ?','%'.$word.'%');
                }
            }
            if (isset($search['type']) && strlen($search['type']) > 0) {
                $query->leftJoin('c.CompanyType ct')
                ->andWhere('ct.name = ?',$search['type']);
            }
            if (isset($search['state']) && strlen($search['state']) > 0) {
                $query->andWhere('c.state = ?',$search['state']);
            }
            if (isset($search['workforce']) && strlen($search['workforce']) > 0) {
                $query->andWhere('c.workforce >= ?',$search['workforce']);
            }
            // --

            $query->orderBy('c.id DESC')
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

    public function getCompanyType($id) {
    
	    try{
			
			$query = Doctrine_Query::create()
			->from('Model_CompanyType c')
			->where('c.id = ?',$id)
			;
			
			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCompanyTypes() {
    
	    try{
			
			$query = Doctrine_Query::create()
			->from('Model_CompanyType c')
			;
			
			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function searchCompanyWithWords($words) {
    	
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Company c');
			
			foreach($words as $word) {
				$query->andWhere('c.name LIKE ? OR c.group_name LIKE ?',array('%'.$word.'%', '%'.$word.'%'));
			}
			$query->limit(15);

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

}