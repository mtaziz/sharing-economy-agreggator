<?php

class SearchController extends App_Controller_Action {


    public function indexAction() {
        $daoAds = new Dao_AdsDao();
        $daoCategory = new Dao_CategoryDao();
        //Récupération des paramètres

        $page = 1;
        if (isset($this->_get['p']) && !empty($this->_get['p']))  {
            $page = $this->_get['p'];
        }

        $filters = array();
        $filters['words'] = '';
        // $filters['distance'] = '3';
        $filters['address_lat'] = '';
        $filters['address_lng'] = '';
        // $filters['sort'] = 'date-desc';
        $filters['category'] = 'all';
        $filters['subcategory'] = 'all';
        // $filters['min_price'] = '';
        // $filters['max_price'] = '';
        $filters['localisation'] = '';
        $filters['address_zipcode'] = '';
        $filters['address_city'] = '';
        $filters['address_department'] = '';

        // $filters['visibility'] = 'all';

        // Set from GET
        if (isset($this->_get['w'])) {
            $filters['words'] = $this->_get['w'];
        }
        
        if (isset($this->_get['localisation'])) { $filters['localisation'] = $this->_get['localisation']; }
        if (isset($this->_get['address_zipcode'])) { $filters['address_zipcode'] = $this->_get['address_zipcode']; }
        if (isset($this->_get['address_city'])) { $filters['address_city'] = $this->_get['address_city']; }
        if (isset($this->_get['address_department'])) { $filters['address_department'] = $this->_get['address_department']; }

        if (isset($this->_get['c']) && !empty($this->_get['c'])) {
            if ($this->_get['c'] == 'all') {
                $filters['category'] = null;
            }else {
                $filters['category'] = $this->_get['c'];
            }
        }
        if (isset($this->_get['sc']) && !empty($this->_get['sc'])) {
            if ($this->_get['sc'] == 'all') {
                $filters['subcategory'] = null;
            }else {
                $filters['subcategory'] = $this->_get['sc'];
            }
        }
        if (isset($this->_get['address_lat']) && !empty($this->_get['address_lat']) && isset($this->_get['address_lng']) && !empty($this->_get['address_lng'])) {
            $filters['address_lat'] = $this->_get['address_lat'];
            $filters['address_lng'] = $this->_get['address_lng'];
        }

        //Recherche
        $ads=$daoAds->getAll($page,$filters);
        
        // Log de la recherche 
        App_Controller_Log::logDb(App_Controller_Log::SECTION_SEARCH, App_Controller_Log::ACTION_result, $this->_session->user['id'],json_encode($filters)); 

                


        // Category
        $categories=$daoCategory->getAll('all','enable');


        $this->view->address_lat=$filters['address_lat'];
        $this->view->address_lng=$filters['address_lng'];
        $this->view->localisation=$filters['localisation'];
        $this->view->address_zipcode=$filters['address_zipcode'];
        $this->view->address_city=$filters['address_city'];
        $this->view->address_department=$filters['address_department'];
        $this->view->words=$filters['words'];
        $this->view->ads=$ads;
        $this->view->category=$filters['category'];
        $this->view->categories=$categories;
    }

    public function verifpostalcodeAction() {

        // Disable view and layout
        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);

        //Récupération du code postal
        $cp = $this->_get['cp'];

        // Recherche des organisation ayant ce code postal
        $daoCzOrganisation = new Dao_CzOrganisationDao();
        $listCp = $daoCzOrganisation->getOrgaByPostalcode($cp);

        if(count($listCp)>0){
            $verif=true;
        }else{
            $verif=false;
        }
       

        $this->_helper->json->sendJson($listCp[0]['domain']);
    }

    public function sAction() {

    	$this->_helper->layout->setLayout('layout');

    	$projectDao = new Dao_ProjectDao();

        $projects=$projectDao->getAll();

        // Récupération de la ville
        if ($this->getRequest()->isGet()) {

            $form = new Form_SearchProject();

            // User form is Valid && Company form is Valid
            if ($form->isValid($this->_get)) {

                // Save
                $arrayCity=$form->getValues();
                $lat=$arrayCity['lat'];
                $lng=$arrayCity['lng'];
                $latlng=$lat.",".$lng;
                $CitySearchInput=$arrayCity['CitySearchInput'];

                $this->view->lat=$lat;
                $this->view->lng=$lng;
                $this->view->geoAdress=$CitySearchInput;

                // On décortique l'adresse à partir des coordonnées GPS

                // On prépare l'URL du géocodeur
                $geocoder = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%s&sensor=false";
                 
                // On prépare notre requête
                $query = sprintf($geocoder,$latlng);
                 
                // On interroge le serveur
                $results = file_get_contents($query);
                 
                // On affiche le résultat
                $data=json_decode($results);
// var_dump($data->{'results'}[0]);exit;
                $xLat = $data->{'results'}[0]->{'geometry'}->{'location'}->{'lat'};
                $xLng = $data->{'results'}[0]->{'geometry'}->{'location'}->{'lng'};
                $xPostalCode = $data->{'results'}[0]->{'address_components'}[6]->{'long_name'};
                $xCity = $data->{'results'}[0]->{'address_components'}[2]->{'long_name'};
                $xDepartmentName = $data->{'results'}[0]->{'address_components'}[3]->{'long_name'};
                $xDepartmentNumber = $data->{'results'}[0]->{'address_components'}[3]->{'short_name'};
                $xRegion = $data->{'results'}[0]->{'address_components'}[4]->{'long_name'};
                $xCountryName = $data->{'results'}[0]->{'address_components'}[5]->{'long_name'};
                $xCountryCode = $data->{'results'}[0]->{'address_components'}[5]->{'short_name'};

                // On affiche les projets au niveau du département pour l'instant
                $projects=$projectDao->getProjectsByDepartment($xDepartmentNumber);



                // Redirection
                // $this->_helper->redirector->gotoUrl('projets/projet-envoye');
            }
        }

        $this->view->projects=$projects;	

    }

}