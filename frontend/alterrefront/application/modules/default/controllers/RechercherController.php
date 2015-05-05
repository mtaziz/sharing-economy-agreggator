<?php

class RechercherController extends App_Controller_Action {


    public function indexAction() {
        $this->_helper->layout->setLayout('layout');
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
        // $projets = new Model_Projet();
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