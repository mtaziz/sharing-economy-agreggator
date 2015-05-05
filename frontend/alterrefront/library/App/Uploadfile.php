<?php
class App_Uploadfile
{
	/**
	 * Uploade un fichier
	 * @param Zend_Form_Element_File $media
	 * @return Ambigous int|boolean Id de l'image si réussi | false si échec
	 */
	public static function uploadfile($filename, $media_id,$filenameArray,$typeUpload)
	{

        $config = Zend_Registry::get('config');
        $url_media=$config->url_media;
        $url_web_media=$config->url_web_media;
        $tmpPath = $config->url_root.'medias/ads';

        if (isset($filenameArray['name']) && !empty($filenameArray['name'])) {
            $image = $filenameArray['name'];
            $hash = uniqid(md5(rand()), true);
            $names = explode('.', $image);
            $ext = $names[count($names) - 1];

            $imagePath = $tmpPath.'/'.$hash;

            $picturesType = array(
                'image/x-png',
                'image/png',
                'image/pjpeg',
                'image/jpeg',
                'image/jpg',
                'image/gif',
                'image/bmp'
            );

            $movieType = array(
                "video/mov",
                "video/avi",
                "video/mpg",
                "video/mpeg"
            );

            $format = null;
            if (in_array(strtolower($filenameArray['type']), $picturesType)) {
                $format = 'picture';
            }else if (in_array(strtolower($filenameArray['type']), $movieType)) {
                $format = 'movie';
            }

// if (is_uploaded_file($filenameArray['tmp_name']))
//   {
//      if (!move_uploaded_file($filenameArray['tmp_name'],$imagePath.'.'.$ext))
//      {
//         var_dump( 'Problème : Impossible de déplacer le fichier dans son répertoire de destination');
//         exit;
//      }
//   }
//   else
//   {
//     var_dump('Problème : Attaque possible par le fichier ');
//     var_dump($_FILES['picture']['name']);
//     exit;
//   }
 


            if (!isset($format) || empty($format)) {
                // $error = $this->view->translate('File must be').' : *.jpeg, *.bmp, *.jpg, *.png or *.gif';
            } else if (move_uploaded_file($filenameArray['tmp_name'],$imagePath.'.'.$ext)) {

// var_dump("image copiée");
                // $this->_resizeOriginal($imagePath, $ext);

            }else {
// var_dump("image pas copiée");
                // $error = $this->view->translate('Error while uploading your file');
            }
            $imagePath = $tmpPath.'/'.$hash.'.jpg';
// exit;
            // Move Logo to Media
            $paths = App_Uploadfile::createUniqueStorage($hash);
            $mediaPath = $paths['path'].$paths['folder'].$hash.'.'.$ext;
            App_Uploadfile::_moveImagesToMedia($imagePath, $mediaPath);

            // var_dump($imagePath);
            // var_dump($mediaPath);exit;
            

            if ($typeUpload=="new_project"){

                //Sauvegarde du média
                $daoMedia = new Dao_MediaDao();
                $newMedia = new Model_CzMedia();
                $newMedia->link = $url_web_media.$paths['folder'].$hash.'.'.$ext;
                $newMedia->name = $hash;
                $newMedia->format = $format;
                $newMedia->type = "project";
                // Update du media en bdd
                $daoMedia->save($newMedia);

            }
            if ($typeUpload=="new_ad"){

                //Sauvegarde du média
                $daoMedia = new Dao_MediaDao();
                $newMedia = new Model_CzMedia();
                $newMedia->link = $url_web_media.$paths['folder'].$hash.'.'.$ext;
                $newMedia->name = $hash;
                $newMedia->format = $format;
                $newMedia->type = "ad";
                // Update du media en bdd
                $daoMedia->save($newMedia);

            }

            if ($typeUpload=="new_avatar"){

                //Sauvegarde du média
                $daoMedia = new Dao_MediaDao();
                $newMedia = new Model_CzMedia();
                $oldMedia = new Model_CzMedia();

                if(isset($media_id) && $media_id!="" && $media_id!=0){
                    $oldMedia = $daoMedia->getMedia($media_id);
                    App_Uploadfile::_deleteImageFromMedia($oldMedia->name);
                    $newMedia = $oldMedia;
                }
                $newMedia->link = $url_web_media.$paths['folder'].$hash.'.'.$ext;
                $newMedia->name = $hash;
                $newMedia->format = $format;
                $newMedia->type = "user";

                // Update du media en bdd
                $daoMedia->save($newMedia);
            }

           
        }

        return $newMedia->id;
	}

    public static function createUniqueStorage($hash = null) {
        
        $config = Zend_Registry::get('config');

        if($hash === null) {
            $hash = md5(uniqid(rand(), true));
        }       
        
        $path =$config->url_media;
        $folders = substr($hash, 0, 1).'/'.substr($hash, 1, 1).'/'.substr($hash, 2, 1).'/';
        if (!file_exists ($path.$folders)) {
            mkdir($path.$folders, 0777, true);
        }   

        return array('path' => $path, 'folder' => $folders, 'hash' => $hash);
    }

    public static function _moveImagesToMedia($tmpPath, $path) {
        
        if (rename($tmpPath, $path) == false) {
            return "Internal error: rename";
        }
    }

    public static function _deleteImageFromMedia($path) {

        $config = Zend_Registry::get('config');
        $url_media=$config->url_media;

        $mediaPath = $url_media;
        $folders = substr($path, 0, 1).'/'.substr($path, 1, 1).'/'.substr($path, 2, 1).'/';
        App_Uploadfile::execute('rm -f '.$mediaPath.$folders.$path.'*');
    }

    public static function execute($s_commande) {

        $read = null;
        $handle = popen($s_commande.' 2>&1', 'r');

        while( feof($handle) === false ){
            $read .= fread($handle, 8192);
        }

        pclose($handle);
        return($read);
    }

}
