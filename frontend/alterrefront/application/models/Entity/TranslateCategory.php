<?php
// Connection Component Binding
Doctrine_Manager::getInstance()->bindComponent('Model_TranslateCategory', 'doctrine');

/**
 * Model_Entity_TranslateCategory
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @property integer $id
 * @property string $name
 * @property integer $category_id
 * @property integer $language_id
 * @property Model_Category $Category
 * @property Model_Language $Language
 * 
 * @package    ##PACKAGE##
 * @subpackage ##SUBPACKAGE##
 * @author     ##NAME## <##EMAIL##>
 * @version    SVN: $Id: Builder.php 7490 2010-03-29 19:53:27Z jwage $
 */
abstract class Model_Entity_TranslateCategory extends Doctrine_Record
{
    public function setTableDefinition()
    {
        $this->setTableName('translate_category');
        $this->hasColumn('id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => true,
             'autoincrement' => true,
             ));
        $this->hasColumn('name', 'string', 255, array(
             'type' => 'string',
             'length' => 255,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => false,
             'autoincrement' => false,
             ));
        $this->hasColumn('category_id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('language_id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
    }

    public function setUp()
    {
        parent::setUp();
        $this->hasOne('Model_Category as Category', array(
             'local' => 'category_id',
             'foreign' => 'id'));

        $this->hasOne('Model_Language as Language', array(
             'local' => 'language_id',
             'foreign' => 'id'));
    }
}