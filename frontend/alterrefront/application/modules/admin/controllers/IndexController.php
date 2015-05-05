<?php

class Admin_IndexController extends App_Controller_Action {

	public function indexAction() {
	
    $liste=array();
	// Dashboard
	$page = 1;
        // if (isset($this->_get['p'])) {
        //     $page = $this->_get['p'];
        // }

        $daoAd = new Admin_Dao_AdDao();
        $state="'available'";
        $ads = $daoAd->getAdbyState($state,$page,7);

        $daoUser = new Admin_Dao_UserDao();
        $state="'enable'";
        $users = $daoUser->getUserbyState($state,$page);
        // $daoCompany = new Admin_Dao_CompanyDao();
        // $state="'disable'";
        // $companies = $daoCompany->getCompanies($state,$page);

        foreach($users as $user){
            $locale = new Zend_Locale('fr_FR');
            $date = new Zend_Date($user->created_at);
            $liste[]=array(
                "date"=>$user->created_at,
                "date_title"=>$date->toString(Zend_Date::DATE_LONG,$locale),
                // "date"=>date_format($user->created_at, 'Y/m/d')
                "type"=>"user",
                "title"=>"",
                "description"=> $user->firstname." | ".$user->lastname,
                "id"=> $user->id,
                "email" => $user->email,
                // "picture_thumb" => $user->picture_thumb,
                "media"=>""
            );
        }

         
        foreach($ads as $ad){
            $locale = new Zend_Locale('fr_FR');
            $date = new Zend_Date($ad->created_at);
            $liste[]=array(
                "date"=>$ad->created_at,
                "date_title"=>$date->toString(Zend_Date::DATE_LONG,$locale),
                // "date"=>date_format($ad->created_at, 'Y/m/d'),
                "type"=>"ad",
                "title"=>$ad->title,
                "description"=> $ad->category_id." | ".$ad->price,
                "id"=>$ad->id,
                "email" => "",
                // "picture_thumb" => "",
                "media"=> $ad->Media
            );
        }

        sort($liste);
        $liste = array_reverse($liste);
// var_dump($liste);exit;
        $this->view->liste = $liste;
	}
    public function statsAction() {
        // var_dump("Bien le bonjour !"); exit;
        $dateDebut=0;
        $dateFin=0;

        if (isset($this->_get['date'])){
            $date = $this->_getParam("date");
            $dates = explode ( "-" , $date );

            $dateDebut = trim($dates[0]);
            $this->view->dateDebut = $dateDebut;

            list($month, $day,  $year) = explode('/', $dateDebut);
            $dateDebut = mktime(0, 0, 0, $month, $day, $year);
            $dateDebut = date('Y-m-d H:i:s', $dateDebut);

            $dateFin = trim($dates[1]);
            $this->view->dateFin = $dateFin;

            list($month, $day,  $year) = explode('/', $dateFin);
            $dateFin = mktime(0, 0, 0, $month, $day, $year);
            $dateFin = date('Y-m-d H:i:s', $dateFin);
        }

        // Dashboard
        $daoAd = new Admin_Dao_AdDao();
        $ads = $daoAd->nbAdsByDay($dateDebut, $dateFin);
        
        $this->view->ads = $ads;

        $daoUser = new Admin_Dao_UserDao();
        $users = $daoUser->nbUsersByDay($dateDebut, $dateFin);

        $this->view->users = $users;

    }
    public function statsactiveusersAction(){

        if (isset($this->_get['date'])){
            $date = $this->_getParam("date");
            $dates = explode ( "-" , $date );

            $dateDebut = trim($dates[0]);
            $this->view->dateDebut = $dateDebut;

            list($month, $day,  $year) = explode('/', $dateDebut);
            $dateDebut = mktime(0, 0, 0, $month, $day, $year);
            $dateDebut = date('Y-m-d H:i:s', $dateDebut);

            $dateFin = trim($dates[1]);
            $this->view->dateFin = $dateFin;

            list($month, $day,  $year) = explode('/', $dateFin);
            $dateFin = mktime(0, 0, 0, $month, $day, $year);
            $dateFin = date('Y-m-d H:i:s', $dateFin);
        }
        else{
            $dateDebut="2014-01-01 00:00:00";
            $this->view->dateDebut = "01/01/2014";
            $dateFin="2014-12-30 23:00:00";
            $this->view->dateFin = "12/30/2014";

        }
        

        $daoUser = new Admin_Dao_UserDao();
        $users = $daoUser->nbUsersLoginByDay($dateDebut, $dateFin);
        $cumulUsers=0;
// var_dump($users);exit;
        foreach($users as $i => $user){
            // var_dump($user);exit;
            $cumulUsers+=$user[1];
            $users[$i]['cumul']=$cumulUsers;

        }
// var_dump($users);exit;
        $this->view->users = $users;

    }
    public function statsadsAction(){

        if (isset($this->_get['date'])){
            $date = $this->_getParam("date");
            $dates = explode ( "-" , $date );

            $dateDebut = trim($dates[0]);
            $this->view->dateDebut = $dateDebut;

            list($month, $day,  $year) = explode('/', $dateDebut);
            $dateDebut = mktime(0, 0, 0, $month, $day, $year);
            $dateDebut = date('Y-m-d H:i:s', $dateDebut);

            $dateFin = trim($dates[1]);
            $this->view->dateFin = $dateFin;

            list($month, $day,  $year) = explode('/', $dateFin);
            $dateFin = mktime(0, 0, 0, $month, $day, $year);
            $dateFin = date('Y-m-d H:i:s', $dateFin);
        }
        else{
            $dateDebut="2014-01-01 00:00:00";
            $this->view->dateDebut = "01/01/2014";
            $dateFin="2014-12-30 23:00:00";
            $this->view->dateFin = "12/30/2014";

        }

        $daoAd = new Admin_Dao_AdDao();
        $ads = $daoAd->nbAdsByDay($dateDebut, $dateFin);
        $cumulAds = 0;

        foreach($ads as $i => $ad){
            // var_dump($ad);exit;
            $cumulAds+=$ad[1];
            $ads[$i]['cumul']=$cumulAds;
        }
        
        $this->view->ads = $ads;
        
    }
    public function statsusersAction(){
    
        if (isset($this->_get['date'])){
            $date = $this->_getParam("date");
            $dates = explode ( "-" , $date );

            $dateDebut = trim($dates[0]);
            $this->view->dateDebut = $dateDebut;

            list($month, $day,  $year) = explode('/', $dateDebut);
            $dateDebut = mktime(0, 0, 0, $month, $day, $year);
            $dateDebut = date('Y-m-d H:i:s', $dateDebut);

            $dateFin = trim($dates[1]);
            $this->view->dateFin = $dateFin;

            list($month, $day,  $year) = explode('/', $dateFin);
            $dateFin = mktime(0, 0, 0, $month, $day, $year);
            $dateFin = date('Y-m-d H:i:s', $dateFin);
        }
        else{
            $dateDebut="2014-01-01 00:00:00";
            $this->view->dateDebut = "01/01/2014";
            $dateFin="2014-12-30 23:00:00";
            $this->view->dateFin = "12/30/2014";
        }

        $daoUser = new Admin_Dao_UserDao();
        $users = $daoUser->nbUsersByDay($dateDebut, $dateFin);
        $cumulUsers=0;

        foreach($users as $i => $user){
            $cumulUsers+=$user[1];
            $users[$i]['cumul']=$cumulUsers;
        }

        $this->view->users = $users;
    }
	public function newadsAction() {
		
		// Dashboard
		$page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $daoAd = new Admin_Dao_AdDao();

        $state="'available'";
        $this->view->ads = $daoAd->getAdbyState($state,$page);

        $controller = $this->getRequest()->getControllerName();
        $action = $this->getRequest()->getActionName();

        $this->view->controller = $controller;
        $this->view->action = $action;
	}
	public function newcompaniesAction() {

		// Dashboard
		$page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $daoCompany = new Admin_Dao_CompanyDao();
        $daoUser = new Admin_Dao_UserDao();

        $state="'registered'";
        
        $companies = $daoCompany->getCompanies($state,$page);
        $usersAdmin = "";
        foreach($companies as $i => $company){

            $users = $daoUser->getUserAdminByCompany($company->id);

            foreach($users as $user){
                $userAdmin[$company->id] = $user->email;
            }
        }
        $this->view->registeredCompanies = $companies;
        $this->view->userAdmin = $userAdmin;


        $controller = $this->getRequest()->getControllerName();
        $action = $this->getRequest()->getActionName();

        $this->view->controller = $controller;
        $this->view->action = $action;

	}
	public function newusersAction() {
		$page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

		// Dashboard
		$daoAd = new Admin_Dao_UserDao();
        $this->view->users = $daoAd->getUserbyState(null,$page);
	}

}