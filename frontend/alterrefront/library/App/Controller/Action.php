<?php

// if ('matthieu' == APPLICATION_ENV) {
    require_once($_SERVER['DOCUMENT_ROOT'] . '/../library/Thumb/ThumbLib.inc.php');
// }else{
    // require_once($_SERVER['DOCUMENT_ROOT'] . '/library/Thumb/ThumbLib.inc.php');
// }

class App_Controller_Action extends Zend_Controller_Action {

	protected $_get;
	protected $_post;
	protected $_session;
	protected $_layout;
	
	public function init(){

		$this->_get = $this->getRequest()->getParams();
		$this->_post = $this->getRequest()->getPost();
		$this->_layout = $this->_helper->layout();
		$this->_session = new Zend_Session_Namespace('troovon');


		$config = Zend_Registry::get('config');
		$this->view->config = $config;
		
		$myconf = Zend_Registry::get('myconf');
		$this->view->myconf = $myconf;

		$serverName = explode("/", $_SERVER['REQUEST_URI']);
		list($slashVide,$controllerAgence, $actionAgence) = $serverName;
		
		// $daoCzOrganisation = new Dao_CzOrganisationDao();
  //       $city = $daoCzOrganisation->getCityByName($controllerAgence);
        // putenv("ID_CITY=".$city->orga_id);

        // $var=$this->getRequest()->getParams();
        // $this->_session->id_orga=$var["id_orga"];

  //       $auth = TBS\Auth::getInstance();
		// if ($auth->hasIdentity()) {
		// 	var_dump("loggué");
		// 	var_dump($_SESSION);exit;
		// 		// J'affiche le menu loggué
		// // l'identité existe ; on la récupère
		// 	// $identite = $auth->getIdentity();
		// }else{
		// 	var_dump("non loggué");
		// 	foreach ($_SESSION as $k=>$v) {
  //   			echo "$k => $v <br />\n";
		// 	}	
		// 	var_dump($_SESSION);exit;
		// }


        // Si un cookie de géolocalisation est défini oin redirige vers la page de sa ville
        // if (isset ( $_COOKIE [$config->cookie->ville] ) && ! empty ( $_COOKIE [$config->cookie->ville] )) {
        // 	var_dump("un cookie de ville exist");exit;
        // }

	}
	
	public function adsTmpImagePath() {
		
		$config = Zend_Registry::get('config');
		$tmpPath = $config->url_root.'medias/ads';
		return $tmpPath;
	}
	
	public function companiesTmpImagePath() {
	
		$config = Zend_Registry::get('config');
		$tmpPath = $config->url_root.'medias/companies';
		return $tmpPath;
	}

    public function usersTmpImagePath() {

        $config = Zend_Registry::get('config');
		$tmpPath = $config->url_root.'medias/users';
        return $tmpPath;
    }

	public function _moveImagesToMedia($tmpPath, $path) {
		
		if (rename($tmpPath, $path) == false) {
    		return "Internal error: rename";
    	}
	}

    public function _deleteImageFromMedia($path) {

	    $config = Zend_Registry::get('config');
        $url_media=$config->url_media;

        $mediaPath = $url_media;
        $folders = substr($path, 0, 1).'/'.substr($path, 1, 1).'/'.substr($path, 2, 1).'/';
        $this->execute('rm -f '.$mediaPath.$folders.$path.'*');
    }

	public function createUniqueStorage($hash = null) {
	    
	    $config = Zend_Registry::get('config');
        $url_media=$config->url_media;
		if($hash === null) {
			$hash = md5(uniqid(rand(), true));
		}		
		
		$path = $url_media;
		$folders = substr($hash, 0, 1).'/'.substr($hash, 1, 1).'/'.substr($hash, 2, 1).'/';
		if (!file_exists ($path.$folders)) {
			mkdir($path.$folders, 0777, true);
		}	

		return array('path' => $path, 'folder' => $folders, 'hash' => $hash);
	}

	 public function _createUserThumbnail($imagePath, $thumbPath) {

        // Resize picture
        $image = PhpThumbFactory::create($imagePath);
        $image->resize(640, 480);
        $image->save($imagePath);

        // Resize thumb
        $thumb = PhpThumbFactory::create($thumbPath);
        $thumb->adaptiveResize(70, 70);
        $thumb->save($thumbPath);
    }

	
	private function execute($s_commande) {

        $read = null;
        $handle = popen($s_commande.' 2>&1', 'r');

        while( feof($handle) === false ){
            $read .= fread($handle, 8192);
        }

	    pclose($handle);
	    return($read);
    }
	
	protected function requiredParams($required, $method = 'post') {
		
		$error = array();
		$error["error"] = "";
		
		foreach($required as $key) {
			
			if ($method == 'post') {
			
				if (!isset($this->_post[$key]) || empty($this->_post[$key])) {
					$error["error"] = $error["error"]." ".$key." parameter is required";
				}
			
			}else {
			
				if (!isset($this->_get[$key]) || empty($this->_get[$key])) {
					$error["error"] = $error["error"]." ".$key." parameter is required";
				}
			}
		}
		
		if (strlen($error["error"]) > 0) {
			return $error;
		}
		
		return true;
	}
	
	protected function replaceNullByString(&$array) {
		array_walk_recursive($array, array($this, 'processingNullByString'));
	}
	
	private function processingNullByString(&$item, $key) {
		if ($item === null) {
			$item = "";
		}
	}

}
