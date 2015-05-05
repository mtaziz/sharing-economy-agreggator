<?php

class UserController extends App_Controller_Action
{

    public function signupValidatedAction() {

        $config = Zend_Registry::get('config');

        $this->view->headTitle($this->view->translate('Activation de votre compte').' - Coosome.com');

        if (isset($this->_get['h']) && !empty($this->_get['h']) && isset($this->_get['u']) && !empty($this->_get['u'])) {
            
            $daoUser = new Dao_UserDao();
            $user = $daoUser->getUser($this->_get['u']);

            // User Exist
            if (isset($user->id) && !empty($user->id) && $user->confirm_hash === $this->_get['h']) {
                
                if ($user->state == 'enable') {
                    $this->view->error = $this->view->translate('Your account was already activated');

                }else {

                    // Activate his Account
                    $user->state = 'enable';
                    $daoUser->save($user);


                        $title = $this->view->translate('Mot de passe réinitialisé - Coosome.com');
                        $link=$config->url.'/reinitialisation-du-mot-de-passe?h='.$user->confirm_hash.'&u='.$user->id;

                    $content="
Bienvenue sur ".$config->cookie->name.",<br><br>

Avec succès, vous venez de vous inscrire sur ".$config->cookie->name.".<br><br>
<i>Rappel de vos identifiants:</i><br>
Votre login : <b>".$user->email."</b><br>
Votre mot de passe : <i>Transmis dans l'email d'activation</i><br><br>

<i>Note :</i><br>
Votre mot de passe est sécurisé. En cas d'oubli, vous pouvez le réinitialiser <a href='".$link."'>ICI</a><br><br>

A tout de suite sur ".$config->cookie->name." !<br><br>
L'équipe ".$config->cookie->name."<br>
<a href='".$config->url."'>".$config->cookie->domain."</a>
";
                    $mail = new Zend_Mail('UTF-8');
                    $mail->setBodyHtml($content)
                        ->setFrom($config->noReply, $config->url)
                        ->addTo($user->email, $user->firstname. " ".$user->lastname)
                        ->setSubject($title)
                        ->send();


                    $mail = new Zend_Mail('UTF-8');
                    $mail->setBodyText('Nouveau membre actif :<b> '.$user->firstname." ".$user->lastname."</b> (".$user->email.")  le ".date('Y-m-d H:i:s',time()))
                        ->setFrom($config->noReply, $config->url)
                        ->addTo($config->email_technique)
                        ->setSubject("Inscription utilisateur ".$config->cookie->name)
                        ->send();
                }
            }else {
                $this->view->error = 'Error while trying to activate your account';
            }
        }else {
            $this->_redirect('/');
        }
    }
    public function profilAction() {
        
        if(isset($this->_session->user['id'])){
            $daoUser = new Dao_UserDao();
            $user = $daoUser->getUser($this->_session->user['id']);
            $this->user=$user;
        }
    }

    public function dashboardAction() {
        
        if(isset($this->_session->user['id'])){
            // user
            $daoUser = new Dao_UserDao();
            $user = $daoUser->getUser($this->_session->user['id']);

            // Projects
            $projectDao = new Dao_ProjectDao();
            $projects=$projectDao->getMyProjects($this->_session->user['id'],"projet");
            $adsPropositions=$projectDao->getMyProjects($this->_session->user['id'],"annonce","proposition");
            $adsBesoins=$projectDao->getMyProjects($this->_session->user['id'],"annonce","besoin");

            //ads



            $this->view->propositions=$adsPropositions;
            $this->view->besoins=$adsBesoins;
            $this->view->projects=$projects;
            $this->user=$user;
        }
    }

    public function inscriptionAction() {

        $config = Zend_Registry::get('config');
        $URL=$config->url;

        $form = new Form_Signup();
        $user = new Model_User();

        $redirection =$_SERVER['HTTP_REFERER'];

        if ($this->getRequest()->isPost()) {

            // User form is Valid 
            if ($form->isValid($this->_post)) {
                $values = $form->getValues();
                    
                // Si mail ok on vérifie s'il a deja un compte
                $daoUser = new Dao_UserDao();
                $user = $daoUser->getUserByEmail($values['email']);

                // Si email existant, on update son confirm_hash
                if (isset($user->id)) {
                    //TODO : envoyer un mail à support@citeez.com en indiquant qu'un forçage de connexion a été tenté

                // Sinon on enregistre le nouvel user
                }else {
                    $user = new Model_User();
                    // Save user
                    $user->fromArray($values);
                    
                    $user->language_id = 7;
                    // $user->language_id = FO_LANG;
                    $user->confirm_hash = uniqid(md5(rand()), true);
                    $user->state = 'waitingEmailConfirm';
                    $user->created_at =Date('Y-m-d H:i:s', time());

                    $user->password=md5($this->_post["password"]);
                    $daoUser->save($user);

                    $link=$URL.'/activation?h='.$user->confirm_hash.'&u='.$user->id;

                    $content="
Bienvenue sur ".$config->cookie->name."<br><br>


Afin de finaliser votre inscription sur ".$config->cookie->name.", une toute dernière opération : merci de cliquer sur le bouton ci-dessous :<br>".$link."<br><br>
Cela permet simplement de valider votre compte. Vous pourrez ensuite découvrir votre nouveau service.<br>
<i>Cela ne fonctionne pas ? Copiez collez le lien suivant dans votre navigateur !</i><br><br>

<i>Rappel de vos identifiants:</i><br>
Votre login : <b>".$user->email."</b><br>
Votre mot de passe : <b>".$this->_post["password"]."</b><br><br>


A très vite sur ".$config->cookie->name." ! <br><br>
L'équipe ".$config->cookie->name."<br>
<a href='".$config->url."'>".$config->cookie->domain."</a>
";
                    $mail = new Zend_Mail('UTF-8');
                    $mail->setBodyHtml($content)
                        ->setFrom($config->noReply, $config->url)
                        ->addTo($user->email, $user->firstname. " ".$user->lastname)
                        ->setSubject("Bienvenue sur ".$config->cookie->name)
                        ->send();


                    // $content = "Un nouvel utilisateur s'est inscrit, il doit maintenant cliquer sur le lien d'activation reçu dans sa boite mail pour continuer
                    //         <br><br>Son email est : ".$user->email."<br>
                    //             Date d'inscription : ".date('Y-m-d H:i:s',time());

                    // $lemail='inscription@troovon.com';
                    // $this->sendMail("Nouvel utilisateur inscrit", $content, array($lemail), true);

                    // $options = array(
                    //     'controller' => 'user',
                    //     'action' => 'signupconfirmsuccess',
                    //     'module' => 'pro',
                    // );
                    $this->getResponse()->setRedirect('/inscription-envoyee');
                }
            }

        }
        // redirection si echec
        $this->getResponse()->setRedirect($redirection);
    }

    public function verifemailAction() {

        // Disable view and layout
        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);

        // Recherche des users ayant cet email
        $daoUser = new Dao_UserDao();
        $user = $daoUser->getUserByEmail($_GET['email']);

        if(isset($user->id)){
           $verif=true; 
        }else{
            $verif=false;
        }
       
        $this->_helper->json->sendJson($verif);
    }


    public function loginAction()
    {
        $auth = TBS\Auth::getInstance();

        $providers = $auth->getIdentity();

        // Here the response of the providers are registered
        if ($this->_hasParam('provider')) {
            $provider = $this->_getParam('provider');
            switch ($provider) {
                case "facebook":
                    if ($this->_hasParam('code')) {
                        $adapter = new TBS\Auth\Adapter\Facebook(
                                $this->_getParam('code'));
                        $result = $auth->authenticate($adapter);
                    }
                    if($this->_hasParam('error')) {
                        throw new Zend_Controller_Action_Exception('Facebook login failed, response is: ' . 
                            $this->_getParam('error'));
                    }
                    break;
                // case "twitter":
                //     if ($this->_hasParam('oauth_token')) {
                //         $adapter = new TBS\Auth\Adapter\Twitter($_GET);
                //         $result = $auth->authenticate($adapter);
                //     }
                //     break;
                // case "google":
                
                //     if ($this->_hasParam('code')) {
                //         $adapter = new TBS\Auth\Adapter\Google(
                //                 $this->_getParam('code'));
                //         $result = $auth->authenticate($adapter);
                //     }
                //     if($this->_hasParam('error')) {
                //         throw new Zend_Controller_Action_Exception('Google login failed, response is: ' . 
                //             $this->_getParam('error'));
                //     }
                //     break;

            }
            // What to do when invalid
            if (isset($result) && !$result->isValid()) {
                $auth->clearIdentity($this->_getParam('provider'));
                throw new Zend_Controller_Action_Exception('Login failed');
            } else {
                 $this->_helper->redirector->gotoUrl('/user/connexion');
            }
        } else { // Normal login page
            // $this->view->googleAuthUrl = TBS\Auth\Adapter\Google::getAuthorizationUrl();
            // $this->view->googleAuthUrlOffline = TBS\Auth\Adapter\Google::getAuthorizationUrl(true);
            $this->view->facebookAuthUrl = TBS\Auth\Adapter\Facebook::getAuthorizationUrl();

            // $this->view->twitterAuthUrl = \TBS\Auth\Adapter\Twitter::getAuthorizationUrl();
        }

    }
    public function connectAction()
    {
        $auth = TBS\Auth::getInstance();
        if (!$auth->hasIdentity()) {
            throw new Zend_Controller_Action_Exception('Not logged in!', 404);
        }
        $this->view->providers = $auth->getIdentity();
    }

    public function logoutAction()
    {
        // \TBS\Auth::getInstance()->clearIdentity();
        Zend_Auth::getInstance()->clearIdentity();
        TBS\Auth::getInstance()->clearIdentity();
        Zend_Session::namespaceUnset('troovon');
        $this->_redirect('/');
    }


    public function connexionAction() {

        // Si connexion FB on crée le user dans la base à partir de ses infos FB
        $auth = TBS\Auth::getInstance();

        if(isset($this->_post['url_edition_connexion']) && $this->_post['url_edition_connexion']!=""){
            $redirection=$this->_post['url_edition_connexion'];
        }else{
            $redirection =$_SERVER['HTTP_REFERER'];
        }

        if (!$auth->hasIdentity()) {

            //Sinon processus d'inscription normal via ZEND

            if ($this->getRequest()->isPost()) {

                if (!isset($this->_post['login_email']) || empty($this->_post['login_email'])) {
                    // var_dump($this->view->translate('Please check your login / password'));
                    return;
                }else if (!isset($this->_post['login_password']) || empty($this->_post['login_password'])) {
                    // var_dump($this->view->translate('Please check your login / password'));
                    return;
                }

                $dbAdapter = new App_Auth_Adapter_Doctrine( Doctrine::getConnectionByTableName('user') );

                $dbAdapter->setTableName('Model_User u')
                    ->setIdentityColumn('u.email')
                    ->setCredentialColumn('u.password')
                    ->setCredentialTreatment('MD5(?)')
                    ->setIdentity( $this->_post['login_email'] )
                    ->setCredential( $this->_post['login_password'] );
                $auth = Zend_Auth::getInstance();
                $result = $auth->authenticate( $dbAdapter );
                $user = $dbAdapter->getResultRowObject(null, array('password'));

                // Verify Privilege, State and Company subscription
                $canLogin = true;
                $daoUser = new Dao_UserDao();
                $modelUser = new Model_User();

                if (isset($user) && !empty($user->id)) {
                    $modelUser = $daoUser->getUser($user->id);
                    // Check first connection
                    if(!$modelUser->last_connection){
                         $this->_session->firstConnection = true;
                         // $redirection="/actions";
                    }else{
                        $this->_session->firstConnection = false;
                    }

                    if ($modelUser->state != 'enable') {

                        $canLogin = false;
                        $errorMessage = $this->view->translate('Your account was not activated');
                        // On log l'action
                        $daoLog = new Dao_LogDao();
                        $log = new Model_Log();
                        $log->user_id = $user->id;
                        //$log->company_id = 1;
                        $log->section = "login";
                        $log->action = "login";
                        //$log->langue = "1";
                        $log->variable = $errorMessage;
                        //$log->commentaire = "1";
                        $daoLog->save($log);

                    }

                }else{
                    // var_dump("user inexistant ou mauvais login/pass");
                }

                if ($result->isValid() === true && $canLogin) {

                    $auth->getStorage()->write($res = $dbAdapter->getResultRowObject(null, array('password')));

                    // Remember Me
                    if (isset($this->_post['remember']) && !empty($this->_post['remember'])) {
                        Zend_Session::rememberUntil(518400);
                    }else {
                        Zend_Session::rememberUntil(3600);
                    }
                        // On log l'action
                        $daoLog = new Dao_LogDao();
                        $log = new Model_Log();
                        $log->user_id = $modelUser->id;
                        // $log->company_id = $modelUser->UserCompany[0]->Company->id;
                        $log->section = "login";
                        $log->action = "login ok";
                        //$log->langue = "1";
                        $log->variable = $modelUser->email;
                        $log->commentaire = "Dernière connection : ".$modelUser->last_connection;
                        $daoLog->save($log);

                    // Save user in session
                    $session = new Zend_Session_Namespace('troovon');
                    $session->modelUser = $modelUser;
                    $session->user['provider_name'] = $modelUser->provider_name;
                    $session->user['id'] = $modelUser->id;
                    $session->user['email'] = $modelUser->email;
                    $session->user['firstname'] = $modelUser->firstname;
                    $session->user['fullname'] = $modelUser->getFullname();
                    $session->user['lastConnection'] = strtotime($modelUser->last_connection);

                    // Update last connection date
                    $modelUser->last_connection = date('Y-m-d H:i:s');
                    $daoUser->save($modelUser);

                    $this->getResponse()->setRedirect($redirection);

                    // $this->_redirect("/");

                    // Redirige vers l'url demandé initialement
                    // $session = new Zend_Session_Namespace('lastRequest');
                    // if (isset($session->lastRequestUri) && $session->lastRequestUri!="/") {
                        // if ($modelUser->UserCompany[0]->Company->showOrgaPage=="1"){
                            
                        //     // Orga Infos
                        //     $domain="/";
                        //     // $domain="/ad/company";
                        //     $daoCzOrganisation = new Pro_Dao_OrgaInfoDao();
                        //     // $orgaInfos = $daoCzOrganisation->getOrga($modelUser->UserCompany[0]->Company->id);
                        //     if(!empty($orgaInfos["domain"]) && $orgaInfos["domain"]!=""){
                        //         $domain= $orgaInfos["domain"];
                        //     }
                        //     $this->_redirect($redirection);
                        //     // $this->_redirect("$domain");
                            


                        // }
                        // $this->_redirect($redirection);
                        // return;
                    // }else {
                    //     // Si un domain est défini pour son entreprise on redirige dessus, sinon redirection sur index
                    //     // Infos de l'organisation
                    //     if ($modelUser->UserCompany[0]->Company->showOrgaPage=="1"){
                    //         // Orga Infos
                    //         $domain="/";
                    //         // $domain="/ad/company";
                    //         $daoCzOrganisation = new Pro_Dao_OrgaInfoDao();
                    //         $orgaInfos = $daoCzOrganisation->getOrga($modelUser->UserCompany[0]->Company->id);
                    //         if(!empty($orgaInfos["domain"]) && $orgaInfos["domain"]!=""){
                    //             $domain= $orgaInfos["domain"];
                    //         }
                    //         $this->_redirect($redirection);
                    //         // $this->_redirect("$domain");
                    //     }else{
                    //         $this->_redirect($redirection);
                    //     }

                    // }

                } else {

                    switch ( $result->getCode() ) {

                        case Zend_Auth_Result::FAILURE_IDENTITY_NOT_FOUND:
                        case Zend_Auth_Result::FAILURE_CREDENTIAL_INVALID:
                            $error = $this->view->translate('Please check your login / password');
                            break;

                        default:
                            if (!$canLogin) {
                                $error = $errorMessage;
                            }else{
                                $error = $this->view->translate('Error please try later');
                            }
                            break;
                    }

                    $auth->clearIdentity();
                    $this->view->error = $error;
                    $this->_redirect($redirection);
                }
            }
            // throw new Zend_Controller_Action_Exception('Not logged in!', 404);
        }else{
            //Connecté via FB
            $providers = $auth->getIdentity();
            foreach ($providers as $provider){
                $provider_name=$provider->getName();
                $provider_id=$provider->getId();
                $profile = $provider->getApi()->getProfile();
                $provider_picture=$provider->getApi()->getPicture();
            }


            $daoUser = new Dao_UserDao();
            $user = new Model_User();
            // On verifie le provider et l'id (index) s'ils sont présent dans la table user
            // $user = $daoUser->getUserByProvider($provider_name,$provider_id);

            $user = $daoUser->getUserByEmail($profile["email"]);

            if (isset($user) && !empty($user->id)) {
                //Si oui je met à jour ses infos
                $user->lastname = $profile["last_name"];
                $user->firstname = $profile["first_name"];
                $user->email = $profile["email"];
                $user->updated_at = Date('Y-m-d H:i:s', time());
                $user->state = "enable";
                $user->provider_name = $provider_name;
                $user->provider_id = $profile["id"];
                $user->provider_gender = $profile["gender"];
                $user->provider_link = $profile["link"];
                $user->provider_locale = $profile["locale"];
                $user->provider_timezone = $profile["timezone"];
                $user->provider_picture = $provider_picture;
                $daoUser->save($user);
            }else{
                $user = new Model_User();
                //Sinon je l'incris
                $user->lastname = $profile["last_name"];
                $user->firstname = $profile["first_name"];
                $user->email = $profile["email"];
                $user->created_at = Date('Y-m-d H:i:s', time());
                $user->language_id = 7;
                $user->state = "enable";
                $user->provider_name = $provider_name;
                $user->provider_id = $profile["id"];
                $user->provider_gender = $profile["gender"];
                $user->provider_link = $profile["link"];
                $user->provider_locale = $profile["locale"];
                $user->provider_timezone = $profile["timezone"];
                $user->provider_picture = $provider_picture;
                $daoUser->save($user);
            }

            //Enregistrement de la photo de profil

            // Enregistrement des infos en session
            Zend_Session::rememberUntil(518400);

            // Save user in session
            $session = new Zend_Session_Namespace('troovon');
            $session->modelUser = $user;
            $session->user['provider_picture'] = $provider_picture;
            $session->user['provider_name'] = $user->provider_name;
            $session->user['id'] = $user->id;
            $session->user['email'] = $user->email;
            $session->user['firstname'] = $user->firstname;
            $session->user['fullname'] = $user->getFullname();
            $session->user['lastConnection'] = strtotime($user->last_connection);

            //Redirection
            $this->getResponse()->setRedirect($redirection);
           
        }

    }

 public function resetPasswordAction() {

        $this->view->headTitle($this->view->translate('Forgotten password ?').' - Citeez');

        $this->view->show_signin = true;
        $config = Zend_Registry::get('config');

        $form = new Form_ResetPwdValid();
        $form->setAction('/mot-de-passe-oublie');
        $this->view->form = $form;

        // Submit reset form
        if ($this->getRequest()->isPost()) {

            if ($form->isValid($this->_post)) {

                $daoUser = new Dao_UserDao();
                $user = $daoUser->getUserByEmail($this->_post['email']);

                // User Exist and activate
                if (isset($user->id) && !empty($user->id)) {

                    if ($user->state == 'enable') {

                        // Reset passord
                        $user->confirm_hash = uniqid(md5(rand()), true);
                        $daoUser->save($user);

                        // Send email
                        $lang = 'en';
                        if ($this->_session->lang->type == 'fr-FR') { $lang = 'fr'; }

                        $title = $this->view->translate('Réinitialisation du mot passe - Coosome.com');
                        $link=$config->url.'/reinitialisation-du-mot-de-passe?h='.$user->confirm_hash.'&u='.$user->id;

                    $content="
Bonjour,<br><br>

Vous souhaitez changer votre mot de passe ou vous l’avez perdu ? Pas de panique, tout va bien se passer !<br>
Il vous suffit de cliquer sur le lien suivant :<br><br>".$link."<br><br>

Nous vous souhaitons de nombreux partages sur ".$config->cookie->name." !<br><br>
L'équipe ".$config->cookie->name."<br>
<a href='".$config->url."'>".$config->cookie->domain."</a>
";
                    $mail = new Zend_Mail('UTF-8');
                    $mail->setBodyHtml($content)
                        ->setFrom($config->noReply, $config->url)
                        ->addTo($user->email, $user->firstname. " ".$user->lastname)
                        ->setSubject($title)
                        ->send();




                       // $this->_helper->redirector('reset-finish', 'user');
                        $this->getResponse()->setRedirect('/mot-de-passe-oublie-envoye');
                        // $this->_redirector->gotoRoute(array(), 'reset-pwd-confirm');

                        // $this->_helper->redirector('reset-pwd-confirm','user');

                    }else {
                        $this->view->error = $this->view->translate('Veuillez cliquer sur le lien d\'activation reçu par mail avant de réinitialiser votre mot de passe');
                    }
                }else {
                    $this->view->error = $this->view->translate("Votre email est inconnu.");
                }
            }else{
                $this->view->error = $this->view->translate("Veuillez renseigner votre email.");
            }
        }
    }
    public function resetPasswordConfirmAction() {
        $this->view->headTitle($this->view->translate('Forgotten password ?').' - Citeez');
    }

    public function resetValidAction() {

        $config = Zend_Registry::get('config');

        $this->view->headTitle($this->view->translate('Reset password').' - Citeez');

        $this->view->show_signin = true;

        $form = new Form_ResetPwd();
        $form->setAction('/reinitialisation-du-mot-de-passe');

        // $this->view->errorStatus ='alert-error';

        // Submit reset form
        if ($this->getRequest()->isPost()) {

            if ($form->isValid($this->_post)) {
                $daoUser = new Dao_UserDao();
                $user = $daoUser->getUser($this->_post['u']);

                // User Exist and activate
                if (isset($user->id) && !empty($user->id) && $user->confirm_hash === $this->_post['h']) {

                    if ($user->state == 'enable') {
                        // Reset password
                        $user->password = md5($this->_post['password']);
                        $daoUser->save($user);

                        $title = $this->view->translate('Mot de passe réinitialisé - Troovon');
                        $link=$config->url.'/reinitialisation-du-mot-de-passe?h='.$user->confirm_hash.'&u='.$user->id;

                    $content="
Bonjour,<br><br>

Votre mot de passe a été modifié, le voici : [".$this->_post['password']."] !<br><br>
Suite à votre demande, votre mot de passe ".$config->cookie->name." vient d'être réinitialisé.<br>
Si vous n’avez fait aucune demande de modification de votre mot de passe, merci de nous le signaler rapidement en cliquant sur ce lien : <a href='mailto:".$config->email_technique."'>Faire un signalement</a><br><br>

Nous vous souhaitons de nombreux partages sur ".$config->cookie->name." !<br><br>
L'équipe ".$config->cookie->name."<br>
<a href='".$config->url."'>".$config->cookie->domain."</a>
";
                    $mail = new Zend_Mail('UTF-8');
                    $mail->setBodyHtml($content)
                        ->setFrom($config->noReply, $config->url)
                        ->addTo($user->email, $user->firstname. " ".$user->lastname)
                        ->setSubject($title)
                        ->send();


                        $this->getResponse()->setRedirect('/');

                    }else {
                        $this->view->error = 'Please active your account before reset your password.';
                    }
                }else {
                    $this->view->error = 'Error, you don\'t have access to this page.';
                }
            }

        }elseif(isset($_GET['h']) && !empty($_GET['h']) && isset($_GET['u']) && !empty($_GET['u'])) {

            $form->u->setValue($_GET['u']);
            $form->h->setValue($_GET['h']);

        }else {

            // $this->_helper->redirector("pro");
            $this->_redirect("/");
        }

        $this->view->form = $form;
    }


    public function saveuserAction() {

        $config = Zend_Registry::get('config');
        $url_media=$config->url_media;
        $url_web_media=$config->url_web_media;
        if ($this->getRequest()->isPost()) {

            $form = new Form_User();
            $daoUser = new Dao_UserDao();
            $daoAddress = new Dao_CzAddressDao();
            $user = new Model_User();
            $user = $daoUser->getUser($this->_session->user['id']);

            // Do not edit password and state
            $form->removeElement('email');
            $form->removeElement('password');
            $form->removeElement('state');

            if ($form->isValid($this->_post)) {

                $values = $form->getValues();
                $user->fromArray($values);

                // Sauvegarde de la date de naissance
                if($_POST["dd"]!="" && $_POST["mm"]!="" && $_POST["yyyy"]!=""){
                    $dd=$_POST["dd"];
                    $mm=$_POST["mm"];
                    $yyyy=$_POST["yyyy"];
                    $birthdate=$yyyy."-".$mm."-".$dd;
                    $user->birthdate=$birthdate;
                }

                //Sauvegarde de l'image de profil
                if($_FILES["picture"]["error"]==0){
                    $media_id = App_Uploadfile::uploadfile("picture",$user->media_id,$_FILES["picture"],"new_avatar");   
                    $user->media_id=$media_id;
                }

                // Sauvegarde de l'adresse
                $address = new Model_CzAddress();
                if($user->address_id!=0){
                    $address=$daoAddress->getAddress($user->address_id);
                }

                $addressPost=$this->_post["address"];
                if(isset($addressPost) && $addressPost!="" && $addressPost!=$user->CzAddress->address){

                    $address->title=$this->_post["address"];
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

                    $daoAddress->save($address);

                    $user->address_id=$address->id;
                }

                $newuser=$daoUser->save($user);

                $this->_helper->redirector->gotoUrl('/user/profil?sav=profil-ok');



        


                // Update Address
                /*
                if (isset($this->_post['cityid']) && $this->_post['cityid'] > 0) {

                    // Verify if the address is an address of the user
                    $canEditAddress = false;
                    foreach ($user->Address as $address) {
                        if ($address->id == $this->_post['cityid']) {
                            $canEditAddress = true;
                        }
                    }

                    if ($canEditAddress) {
                        $address = $daoUser->getAddress($this->_post['cityid']);
                        $address->city = $this->_post['city'];
                        $address->zipcode = $this->_post['zipcode'];
                        if ($this->_post['country'] > 0) {
                            $address->country_id = $this->_post['country'];
                        }
                        $daoUser->save($address);
                    }
                }
                // Create an address
                else if ((isset($this->_post['city']) && strlen($this->_post['city']) > 0) || (isset($this->_post['zipcode']) && strlen($this->_post['zipcode']) > 0)) {

                    $address = new Model_Address();
                    $address->user_id = $user->id;
                    $address->title = $this->view->translate('Address');
                    $address->city = $this->_post['city'];
                    $address->zipcode = $this->_post['zipcode'];
                    if ($this->_post['country'] > 0) {
                        $address->country_id = $this->_post['country'];
                    }

                    $daoUser->save($address);
                }
                */

            }else {
                // var_export($form->getErrors());
            }
        }
        // exit;
        $this->getResponse()->setRedirect('/user/profil?sav=profil-ok');
    }

 public function savepasswordAction() {

        $config = Zend_Registry::get('config');
        $url_media=$config->url_media;
        $url_web_media=$config->url_web_media;
        if ($this->getRequest()->isPost()) {

            $form = new Form_Password();
            $daoUser = new Dao_UserDao();
            $user = $daoUser->getUser($this->_session->user['id']);


            if ($form->isValid($this->_post)) {

                //Enregistrement du nouveau mot de passe s'il n'est pas vide et si l'ancien est OK
                if(isset($this->_post["oldPwd"]) && $this->_post["oldPwd"]!="" && md5($this->_post["oldPwd"])==$user->password){
                    // Si les mots de passe "new" et "confirm" sont identiques ont les sauvegarde
                    if(isset($this->_post["newPwd"]) && $this->_post["newPwd"]!="" && $this->_post["newPwd"]==$this->_post["confirmPassword"]){
                        $user->password=md5($this->_post["newPwd"]);
                        $message='password-ok';
                    }else{
                        $message='password-different';
                    }

                }else{
                    $message='password-ko';
                }
                $daoUser->save($user);
            }
        }
        $this->getResponse()->setRedirect("/user/profil?sav=".$message);
    }


    public function signupSentAction() {
        $this->view->headTitle($this->view->translate('Inscription envoyée').' - Citeez');
    }


    public function writeAction() {

        // Disable view and layout
        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);
        $success="ko";

        //Récupération
        $msg = $this->_post['msg'];
        $projectId = $this->_post['projectId'];
        $userId = $this->_post['userId'];

        //Récupération des parametres de l'emetteur (seuls les membres connectés peuvent écrire aux porteurs de projets)
        if(isset($this->_session->user['id'])){
            $daoUser = new Dao_UserDao();
            $userEmetteur = $daoUser->getUser($this->_session->user['id']);
        
            // Recherche si le destinataire existe
            $daoUser = new Dao_UserDao();
            $userDestinataire = $daoUser->getUser($userId);

            if(count($userDestinataire)>0){


                $projectDao = new Dao_ProjectDao();
                $project=$projectDao->get($idProjet);

                if(count($project)>0){
                

//Envoie du mail au createur du projet
                    $content="
Bonjour,<br><br>


<b>".$user->firstname." ".$user->lastname."</b> vous a envoyé un message sur ".$config->cookie->name." :</b>.<br><br>

<b>".$msg."</b><br><br>


<a href='mailto:".$user->email."'>Répondez-lui dès maintenant</a><br><br>

Nous vous souhaitons de nombreux partages sur ".$config->cookie->name." !<br><br>

L'équipe ".$config->cookie->name."<br>
<a href='".$config->url."'>".$config->cookie->domain."</a>
";
                    $mail = new Zend_Mail('UTF-8');
                    $mail->setBodyHtml($content)
                        ->setFrom($config->noReply, $config->url)
                        ->addTo($project->User->email, $project->User->firstname." ".$project->User->lastname)
                        ->setSubject('Une personne souhaite vous aider sur Citeez')
                        ->send();

                $messageretour='Message envoyé';
                $success="ok";



                }

            }else{
                $messageretour='Le message n\'a pu être envoyé, veuillez contacter notre support pour avoir des explications.';
            }
        }else{
            $messageretour="Vous devez être connecté pour contacter un membre";
        }
        $infos = array('msg' => $messageretour,'success' => $success, );
        $this->_helper->json->sendJson($infos);
    }

}
