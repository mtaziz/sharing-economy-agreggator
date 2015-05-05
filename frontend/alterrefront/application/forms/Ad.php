<?php
class Form_Ad extends Zend_Form {
    
    public function __construct($options = null) {
        parent::__construct($options);
        
        $name = new Zend_Form_Element_Text('name');
        $name->setAttrib('class','fontcolor-blue projectname input-create-project');
        $name->setAttrib('required data-validation-required-message','Le titre de votre projet est important pour intéresser les citoyens');
        $name->setAttrib('required',"");

        $description = new Zend_Form_Element_Textarea('description');
        $description->setAttrib('class','input-create-project');
        $description->setAttrib('placeholder','Description courte de l\'annonce en 140 caractères');
        $description->setAttrib('required',"");
        $description->setAttrib('rows',2);

        $category = new Zend_Form_Element_Select('category');
        $daoCategory = new Dao_CzCategoryDao();
        $categories = $daoCategory->getAll("all","annonce","enable",null);
        foreach ($categories as $categorie) {
            $category->addMultiOption($categorie["id"], $categorie["name"]);
        }
        $category->setAttrib('class','input-create-project');

        $localisation = new Zend_Form_Element_Text('localisation');
        $localisation->setAttrib('class','input-create-project');
        $localisation->setAttrib('placeholder','Ex : Paris, 44000 Nantes, etc.');
        $localisation->setAttrib('required',"");

        $picture = new Zend_Form_Element_File('picture');

        $state = new Zend_Form_Element_Select('state');
        $state->setLabel('state');
        // $state->setMultiOptions(array(
        //     'new' => 'new',
        //     'available' => 'Available',
        //     'treated' => 'Treated',
        //     'expired' => 'Expired',
        //     'deleted_by_user' => 'Delete by user',
        //     'deleted_by_admin' => 'Delete by admin'
        // ));

        $submit = new Zend_Form_Element_Submit('submit');
        $submit->setLabel('Enregistrer');
       
        $this->setAttrib('enctype', 'multipart/form-data');

        $this->addElements(array(
            // $picture,
            $name,
            $description,
            $category,
            $localisation,
            $submit
        ));
    }
    
}