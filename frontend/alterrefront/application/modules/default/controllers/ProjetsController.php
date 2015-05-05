<?php

class ProjetsController extends App_Controller_Action {


    public function indexAction() {
        $daoProjects = new Dao_ProjectDao();

        // On vérifie si une ville est renseignée
        $params=$this->getRequest()->getParams();
        if(isset($params['id_orga']) && $params['id_orga']!=""){
            //Via les paramètres
            $id_orga=$params['id_orga'];
        }

        // elseif(isset($_SESSION['troovon']['id_orga'])){
            //Via la session
            // $id_orga=$_SESSION['troovon']['id_orga'];
        // }

        if(isset($id_orga)){
            // Récupération des coordonnées GPS
            $daoCzOrganisation = new Dao_CzOrganisationDao();
            $orga = $daoCzOrganisation->getCity($id_orga);
            $lat=$orga->CzAddress->latitude;
            $lng=$orga->CzAddress->longitude;
        
            // Récupération des projets déposés dans la zone
            $projects = $daoProjects->getProjectsByCity($orga->CzAddress->zipcode);
            $zoom=13;
        }else{
            // Récupération de tous les projets
            $projects=$daoProjects->getAll();
            $lat="46.52863469527167";
            $lng="2.43896484375";
            $zoom=6;
        }

        $this->view->orga=$orga;
        $this->view->projects=$projects;
        $this->view->lat=$lat;
        $this->view->lng=$lng;
        $this->view->zoom=$zoom;
    }

    public function editionAction() {

        $config = Zend_Registry::get('config');
        $url_media=$config->url_media;
        $url_web_media=$config->url_web_media;


        //Si id est défini c'est le mode d'édition, sinon c'est une création
        if(isset($this->_get['id']) && $this->_get['id']!=""){
            // Edition d'un projet
            $this->view->title="Edition du projet";
            // On vérifie si une ville est renseignée
            $params=$this->getRequest()->getParams();
            if(isset($params['id_orga']) && $params['id_orga']!=""){
                //Via les paramètres
                $daoCzOrganisation = new Dao_CzOrganisationDao();
                $orga = $daoCzOrganisation->getCity($params['id_orga']);
            }

        	$form = new Form_Project();
        	$form->setAction($this->view->link('projets','edition?id='.$this->_get['id']));

            //Récupération du projet
            $projectDao = new Dao_ProjectDao();
            $project=$projectDao->get((int)$this->_get['id']);
            $this->view->project=$project;

            //On préremplie le formulaire
            $form->populate(array(
                'name'=>$project->name,
                'description'=>$project->description,
                'goal'=>$project->goal,
                'category'=>$project->category,
                'partners'=>$project->partners,
                'humanNeed'=>$project->humanNeed,
                'financialNeed'=>$project->financialNeed,
                'materialNeed'=>$project->materialNeed,
                'localisation'=>$project->CzAddress->title,
                'picture'=>$project->CzMedia->link
                ));

        	if ($this->getRequest()->isPost()) {

                
                // User form is Valid && Company form is Valid
                if ($form->isValid($this->_post)) {
                    // Save
                    $projectDao = new Dao_ProjectDao();
                    $address = new Model_CzAddress();
                    $project->fromArray($form->getValues());

                    //Ajout de l'adresse
                    $addressPost=$this->_post["localisation"];
                    if(isset($addressPost) && $addressPost!="" && $addressPost!=$project->CzAddress->title){

                        $address->title=$this->_post["localisation"];
                        $address->address=$this->_post["address_addressLiteral"];
                        $address->zipcode=$this->_post["address_zipcode"];
                        $address->city=$this->_post["address_city"];
                        $address->department_name=$this->_post["address_departmentName"];
                        $address->department_number=$this->_post["address_department"];
                        $address->region=$this->_post["address_regionName"];
                        $address->country_name=$this->_post["address_country"];
                        $address->country_code=$this->_post["address_countryCode"];
                        $address->country_id=1;
                        $address->latitude=$this->_post["address_lat"];
                        $address->longitude=$this->_post["address_lng"];

                        $projectDao->save($address);

                        $project->address_id=$address->id;
                    } 


                    //Sauvegarde des médias
                    if($_FILES["picture"]["error"]==0){
                        $newMediaId = App_Uploadfile::uploadfile("picture","",$_FILES["picture"],"new_project");
                        $project->media_thumb=$newMediaId;
                    }

                    // $project->type="projet";
                    
                    $projectDao->save($project);

                    // Redirection
                    $this->_helper->redirector->gotoUrl('projets/projet-modifie');
                }
            }
        }else{

            // Création d'un nouveau projet
            $this->view->title="Création du projet";
            
            // On vérifie si une ville est renseignée
            $params=$this->getRequest()->getParams();
            if(isset($params['id_orga']) && $params['id_orga']!=""){
                //Via les paramètres
                $daoCzOrganisation = new Dao_CzOrganisationDao();
                $orga = $daoCzOrganisation->getCity($params['id_orga']);
            }

            $form = new Form_Project();
            $form->setAction($this->view->link('projets','edition'));

            if ($this->getRequest()->isPost()) {

                // User form is Valid && Company form is Valid
                if ($form->isValid($this->_post)) {

                    // $form->picture->addFilter('Rename', array('target' => $imagePath, 'overwrite' => true));

                    // Save
                    $projectDao = new Dao_ProjectDao();
                    $project = new Model_CzProject();
                    $address = new Model_CzAddress();

                    $project->fromArray($form->getValues());

                    //Ajout l'auteur
                    $project->creator_id=$this->_session->user['id'];

                    $project->type="projet";

                    //Ajout de l'adresse
                    $addressPost=$this->_post["localisation"];
                    if(isset($addressPost) && $addressPost!=""){

                        $address->title=$this->_post["localisation"];
                        $address->address=$this->_post["address_addressLiteral"];
                        $address->zipcode=$this->_post["address_zipcode"];
                        $address->city=$this->_post["address_city"];
                        $address->department_name=$this->_post["address_departmentName"];
                        $address->department_number=$this->_post["address_department"];
                        $address->region=$this->_post["address_regionName"];
                        $address->country_name=$this->_post["address_country"];
                        $address->country_code=$this->_post["address_countryCode"];
                        $address->country_id=1;
                        $address->latitude=$this->_post["address_lat"];
                        $address->longitude=$this->_post["address_lng"];

                        $projectDao->save($address);

                        $project->address_id=$address->id;
                    } 



                    //Sauvegarde des médias
                    if($_FILES["picture"]["error"]==0){
                        $newMediaId = App_Uploadfile::uploadfile("picture","",$_FILES["picture"],"new_project");
                        $project->media_thumb=$newMediaId;
                    }

                    

                    //Enregistrement du nouveau projet
                    $projectDao->save($project);

                    // Redirection
                    $this->_helper->redirector->gotoUrl('projets/projet-envoye');
                }
            }
        }
        $this->view->orga=$orga;
        $this->view->form=$form;

    }


    public function supprimerunprojetAction() {

        // Disable view and layout
        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);
        $suppression=false;

        // Si l'utilisateur existe et si il est auteur du projet on le supprime
        if(isset($this->_get['id']) && isset($this->_session->user['id'])){
            $projectDao = new Dao_ProjectDao();
            $project=$projectDao->getMyProjects($this->_session->user['id'],"projet",null,$this->_get['id']);

            $projectDao->delete($project);
            $suppression=true;
        }
         $this->_helper->redirector->gotoUrl('/user/dashboard');
        // $this->_helper->json->sendJson($suppression);
    }

    public function projetEnvoyeAction() {
    }   

    public function projetModifieAction() {
    }   

    public function detailsAction() {
        $config = Zend_Registry::get('config');

        $daoProjects = new Dao_ProjectDao();

        $uriToID = explode("/", $_SERVER['REQUEST_URI']);
        $idProjet=$uriToID[3];

        //Récupération du projet
        $projectDao = new Dao_ProjectDao();
        $project=$projectDao->get($idProjet);

        $commentDao = new Dao_CzCommentDao();
        $comments=$commentDao->getCommentsByProject($idProjet);

        if(isset($this->_session->user['id'])){
            $daoUser = new Dao_UserDao();
            $user = $daoUser->getUser($this->_session->user['id']);
        }else{
            $daoUser = new Dao_UserDao();
            $user = $daoUser->getUser(0);
        }
        $this->view->user=$user;


        $this->view->comments=$comments;
        $this->view->project=$project;
        $this->view->url=$config->url;


    }

    public function aiderceprojetAction() {

        // Disable view and layout
        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);
        $success="ko";

        //Récupération du code postal
        $msg = $this->_post['msg'];
        $idProjet = $this->_post['id'];

        //Récupération des parametres de l'emetteur (seuls les membres connectés peuvent écrire aux porteurs de projets)
        if(isset($this->_session->user['id'])){
            $daoUser = new Dao_UserDao();
            $user = $daoUser->getUser($this->_session->user['id']);
        

            // $msg=$msg."<br> Ce message a été envoyé par ".$user->lastname." ". $user->firstname." (".$user->email.")";

            // Recherche des projets ayant cet id
            $projectDao = new Dao_ProjectDao();
            $project=$projectDao->get($idProjet);

            if(count($project)>0){
                
                //Envoie du mail au createur du projet
                    $contentProjet="
Bonjour,<br><br>


<b>".$user->firstname." ".$user->lastname."</b> souhaite vous aider pour votre projet <b>".$project->name."</b> sur Citeez: <br><br>

<i>Son message :</i><br><b>".$msg."</b><br><br>


<a href='mailto:".$user->email."'>Répondez-lui dès maintenant</a><br><br>


Nous vous souhaitons de nombreux partages sur Citeez !<br><br>

L'équipe Citeez<br>
<a href='http://www.citeez.fr'>www.citeez.fr</a>
";

                    $contentAnnonce="
Bonjour,<br><br>


<b>".$user->firstname." ".$user->lastname."</b> vous a envoyé un message sur Citeez concernant votre annonce <b>".$project->name."</b>.<br><br>

<i>Son message :</i><br><b>".$msg."</b><br><br>


<a href='mailto:".$user->email."'>Répondez-lui dès maintenant</a><br><br>

Nous vous souhaitons de nombreux partages sur Citeez !<br><br>

L'équipe Citeez<br>
<a href='http://www.citeez.fr'>www.citeez.fr</a>
";

                    if($project->type=="projet"){$content=$contentProjet;}
                    if($project->type=="annonce"){$content=$contentAnnonce;}

                    $mail = new Zend_Mail('UTF-8');
                    $mail->setBodyHtml($content)
                        ->setFrom('no-reply@citeez.fr', 'Citeez.fr')
                        ->addTo($project->User->email, $project->User->firstname." ".$project->User->lastname)
                        ->setSubject('Une personne souhaite vous aider sur Citeez')
                        ->send();



                $messageretour='Aide envoyée';
                $success="ok";
            }else{
                $messageretour='Le message n\'a pu être envoyé, veuillez contacter notre support pour avoir des explications.';
            }
        }else{
            $messageretour="Vous devez être connecté pour apporter votre aide";
        }
        $infos = array('msg' => $messageretour,'success' => $success, );
        $this->_helper->json->sendJson($infos);
    }


    public function decouvrirLesProjetsAction() {
    	// $this->_helper->layout->setLayout('layout_projets');

    	$projectDao = new Dao_ProjectDao();
        $projects=$projectDao->getAll();

        // Récupération de la ville
        if ($this->getRequest()->isPost()) {

            $form = new Form_SearchProject();

            // User form is Valid && Company form is Valid
            if ($form->isValid($this->_post)) {

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