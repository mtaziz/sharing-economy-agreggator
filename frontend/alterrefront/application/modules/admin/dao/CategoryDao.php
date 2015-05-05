<?php

class Admin_Dao_CategoryDao extends App_Model_Dao {

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
    
    public function getCategory($id, $lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Category c')
			->innerJoin('c.TranslateCategory t')
			->where('c.id = ?',$id)
			->andWhere('t.language_id = ?',$lang)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getCategories($universes = null, $lang = BO_LANG) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Category c');
            if (isset($lang)) {
                $query->innerJoin('c.TranslateCategory t ON c.id = t.category_id AND t.language_id = ?',$lang);
            }

            if (isset($universes)) {
                $query->where('c.universe_id = ?',$universes);
            }
            $query->orderBy('c.position ASC');

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getCategoriesArray($universes = null, $lang = BO_LANG) {

    try{

        $query = Doctrine_Query::create()
            ->from('Model_Category c');
        if (isset($lang)) {
            $query->innerJoin('c.TranslateCategory t ON c.id = t.category_id AND t.language_id = ?',$lang);
        }

        if (isset($universes)) {
            $query->where('c.universe_id = ?',$universes);
        }
       $query->orderBy('c.id ASC');

        return $query->fetchArray();
    }

    catch(Exception $e){
        throw new App_Exception_Model($e->getMessage());
    }
}
    
    public function deleteTranslations($lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->delete('Model_TranslateCategory t')
			->where('t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}