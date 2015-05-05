<?php

class Admin_Dao_UniverseDao extends App_Model_Dao {

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
    
    public function getUniverse($id, $lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Universe u')
			->innerJoin('u.TranslateUniverse t')
            ->leftJoin('u.Category c')
			->where('u.id = ?',$id)
			->andWhere('t.language_id = ?',$lang)
            ->orderBy('u.position ASC, c.position ASC')
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getUniverses($lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Universe u')
			->innerJoin('u.TranslateUniverse t ON u.id = t.universe_id AND t.language_id = ?',$lang)
            ->leftJoin('u.Category c')
            ->orderBy('u.position ASC, c.position ASC')
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getUniversesArray($lang = BO_LANG) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Universe u')
                ->innerJoin('u.TranslateUniverse t ON u.id = t.universe_id AND t.language_id = ?',$lang)
                ->leftJoin('u.Category c')
                ->orderBy('u.position ASC, c.position ASC')
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
			->delete('Model_TranslateUniverse t')
			->where('t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}