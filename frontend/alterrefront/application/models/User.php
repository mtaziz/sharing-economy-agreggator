<?php

/**
 * Model_User
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @package    ##PACKAGE##
 * @subpackage ##SUBPACKAGE##
 * @author     ##NAME## <##EMAIL##>
 * @version    SVN: $Id: Builder.php 7490 2010-03-29 19:53:27Z jwage $
 */
class Model_User extends Model_Entity_User
{

	public function getFullname() {
        return $this->firstname.' '.$this->lastname;
    }
    
 // Test if the user is a member of thiscompany
    public function isMemberOf($company) {

        $isMember = false;
        foreach ($this->UserCompany as $UserCompany) {
            if ($UserCompany->company_id == $company) {
                $isMember = true;
            }
        }
        return $isMember;
    }

    // Test if the user is an admin of the param company
    public function isAdminOf($company) {

        $isAdmin = false;
        foreach ($this->UserCompany as $UserCompany) {
            if ($UserCompany->company_id == $company && $UserCompany->privilege_id == 3) {
                $isAdmin = true;
            }
        }
        return $isAdmin;
    }

    // Test if the user is an SUPER admin of the param company
    public function isSuperAdminOf($company) {

        $isAdmin = false;
        foreach ($this->UserCompany as $UserCompany) {
            if ($UserCompany->company_id == $company && $UserCompany->privilege_id == 1) {
                $isAdmin = true;
            }
        }
        return $isAdmin;
    }

    public function getProfilPicture($width=30,$height=30) {

        if ($this->provider_name=="facebook" && $this->media_id==0) {
            return $_SESSION["troovon"]["user"]["provider_picture"];
        }
        if ($this->provider_name=="zend" && $this->media_id!=0) {
            return  $this->CzMedia->getThumb($width,$height);
        }
        if ($this->media_id==0) {
            return  "";
        }
    }

    // public function getThumbnailPicture($public = false) {

    //     if (strlen($this->picture_thumb) > 0) {
    //         return $this->picture_thumb;
    //     } else if ($public){
    //         return 'http://www.troovon.com/assets/images/pro/picto-profil-empty.png';
    //     } else {
    //         return '/assets/images/pro/picto-profil-empty.png';
    //     }
    // }
}