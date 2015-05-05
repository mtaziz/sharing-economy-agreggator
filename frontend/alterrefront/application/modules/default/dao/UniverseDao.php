<?php

class Dao_UniverseDao extends App_Model_Dao {

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

    public function getUniverse($id, $lang = FO_LANG) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Universe u')
                ->leftJoin('u.Category c')
                ->leftJoin('c.TranslateCategory tc')
                ->leftJoin('u.TranslateUniverse tu')
                ->where('u.id = ?',$id)
                ->andWhere('tc.language_id = ?',$lang)
                ->andWhere('tu.language_id = ?',$lang)
                ->orderBy('u.position ASC, c.position ASC')
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    
    public function getUniverseByCategoryId($categoryId, $lang = FO_LANG) {

        try{

            $query = Doctrine_Query::create()
            ->from('Model_Universe u')
            ->leftJoin('u.Category c')
            ->leftJoin('c.TranslateCategory tc')
            ->leftJoin('u.TranslateUniverse tu')
            ->andWhere('tc.language_id = ?',$lang)
            ->andWhere('tu.language_id = ?',$lang)
            ->andWhere('c.id = ?',$categoryId)
            ->andWhere('c.universe_id = tu.universe_id')
            ->select('*,tu.name as universeName')

            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    public function getUniverses($lang = FO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Universe u')
			->leftJoin('u.Category c')
			->leftJoin('c.TranslateCategory tc')
			->leftJoin('u.TranslateUniverse tu')
			->andWhere('tc.language_id = ?',$lang)
			->andWhere('tu.language_id = ?',$lang)
            ->orderBy('u.position ASC, c.position ASC')
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}