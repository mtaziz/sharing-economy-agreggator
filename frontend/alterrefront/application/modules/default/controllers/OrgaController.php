<?php

class OrgaController extends App_Controller_Action {


    public function indexAction() {
    	// $this->_helper->layout->setLayout('layout_orga');

    	// Récupératoin de l'id_orga via la session
    	$id_orga=$_SESSION['troovon']['id_orga'];

    	// Récupération des coordonnées GPS
    	$daoCzOrganisation = new Dao_CzOrganisationDao();
        $orga = $daoCzOrganisation->getCity($id_orga);

        // Récupération des projets déposés dans la zone
        $daoProject = new Dao_ProjectDao();

        // Si un (ou n) code postal est renseigné on recherche toutes les actions de ce code postal
        $projects = $daoProject->getProjectsByCity($orga->CzAddress->zipcode);


        // sinon, si une liste

		$this->view->projects=$projects;
		$this->view->lat=$orga->CzAddress->latitude;
		$this->view->lng=$orga->CzAddress->longitude;
        // var_dump($this->getRequest()->getParams());exit;
    }

}