<?php

class Admin_Dao_UserDao extends App_Model_Dao {

	public function delete($model) {
    	
    	try{

			$model->delete();
			return true;
		}
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function save($model) {

    	try{

			$model->save();
			return true;
		}
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function searchUsers($search, $page = 1) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_User u');

            // Filters
            if (isset($search['words']) && !empty($search['words']) && count($search['words']) > 0) {
                foreach ($search['words'] as $word) {
                    $query->andWhere('u.lastname LIKE ? OR firstname LIKE ? OR email LIKE ?',array('%'.$word.'%','%'.$word.'%','%'.$word.'%'));
                }
            }
            if (isset($search['company_id']) && $search['company_id'] > 0) {
                $query->innerJoin('u.UserCompany uc')
                    ->andWhere('uc.company_id = ?',$search['company_id']);
            }
            // --

            $query->orderBy('u.id DESC')
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

    public function nbUsersByDay($dateDebut=null, $dateFin=null){

		try{
            $con = Doctrine_Manager::getInstance()->connection();
            if($dateDebut != null && $dateFin != null){ 
                $between = "WHERE created_at BETWEEN '".$dateDebut."' And '".$dateFin."' ";
            }else{ 
                $between = "";
            }

            $st = $con->execute("SELECT created_at, COUNT( created_at ) 
            FROM user
            ".$between."
            GROUP BY YEAR(created_at) ,MONTH( created_at ) , DAY( created_at )");

            return $st->fetchAll();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    public function nbUsersLoginByDay($dateDebut=null, $dateFin=null){
        try{
            $con = Doctrine_Manager::getInstance()->connection();
            if($dateDebut != null && $dateFin != null){ 
                $between = "WHERE l.date BETWEEN '".$dateDebut."' And '".$dateFin."' ";
                $state = " AND l.section = 'login' ";
            }else{ 
                $between = "";
                $state = " WHERE l.section = 'login' ";
            }

            $st = $con->execute("SELECT l.date, COUNT( l.date ) 
            FROM log l
            ".$between.$state."
            GROUP BY YEAR( l.date) ,MONTH( l.date ) , DAY( l.date )");
// var_dump($st);exit;
            return $st->fetchAll();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getUserCompany($company, $user) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_UserCompany uc')
			->where('uc.company_id = ?',$company)
			->andWhere('uc.user_id = ?',$user)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getUserAdminByCompany($companyId) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_User u')
                ->innerJoin('u.UserCompany uc')
                ->andWhere('u.id = uc.user_id')
                ->where('uc.company_id = ?',$companyId)
                ->andWhere('uc.privilege_id = ?',3)
                ->orderBy('uc.user_id ASC')
                ->limit(1)
            ;

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function countRegisteredUsers() {
//anis 03/03/2014
        try{

            $query = Doctrine_Query::create()
                ->from('Model_User c')
                ->where('c.state = ?','enable')
                ->orderBy('c.id DESC')
            ;

            return $query->count();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getAddress($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Address a')
			->where('a.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getAddresses($user) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Address a')
			->where('a.user_id = ?',$user)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getUserByEmail($email) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_User u')
			->where('u.email = ?',$email)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getUserbyState($state=null, $page = 1){
        try{

            $query = Doctrine_Query::create()
            ->from('Model_User u');

            if (isset($state)) {
                $query->where('u.state IN ('.$state.')');
            }

            $query->orderBy('u.id DESC');

            $paginator = new Zend_Paginator(new App_Paginator_Adapter_Doctrine($query));
            $paginator->setItemCountPerPage(25)
                ->setCurrentPageNumber($page);

            return $paginator;
            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
   	}
    
    public function getUser($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_User u')
			->where('u.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getUsers() {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_User u')
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function searchUserWithWords($words) {
    	
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_User u');
			
			foreach($words as $word) {
				$query->andWhere('u.lastname LIKE ? OR u.firstname LIKE ? OR email LIKE ?',array('%'.$word.'%', '%'.$word.'%', '%'.$word.'%'));
			}
			$query->limit(15);

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getUsersByOrgaId($orgaId,$nbUserToShow) {


        try{

            $query = Doctrine_Query::create()
                ->from('Model_User u')
                ->innerJoin('u.UserCompany uc')
                ->Where('u.id = uc.user_id')
                ->andWhere('uc.company_id = ?',$orgaId)
                ->orderBy('u.id DESC')
                ->limit($nbUserToShow)
            ;

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
}