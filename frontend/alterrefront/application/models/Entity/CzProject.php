<?php
// Connection Component Binding
Doctrine_Manager::getInstance()->bindComponent('Model_CzProject', 'doctrine');

/**
 * Model_Entity_CzProject
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @property integer $id
 * @property enum $type
 * @property enum $sousType
 * @property string $name
 * @property string $description
 * @property integer $media_thumb
 * @property integer $address_id
 * @property integer $category
 * @property string $goal
 * @property string $partners
 * @property enum $state
 * @property timestamp $date_add
 * @property timestamp $date_update
 * @property timestamp $startDate
 * @property timestamp $endDate
 * @property string $financialNeed
 * @property string $humanNeed
 * @property string $materialNeed
 * @property integer $creator_id
 * @property Model_CzAddress $CzAddress
 * @property Model_User $User
 * @property Model_CzMedia $CzMedia
 * @property Model_CzCategory $CzCategory
 * @property Doctrine_Collection $CzComment
 * @property Doctrine_Collection $CzProjectCategory
 * @property Doctrine_Collection $CzProjectLeader
 * @property Doctrine_Collection $CzProjectMaterialneed
 * @property Doctrine_Collection $CzProjectMedia
 * 
 * @package    ##PACKAGE##
 * @subpackage ##SUBPACKAGE##
 * @author     ##NAME## <##EMAIL##>
 * @version    SVN: $Id: Builder.php 7490 2010-03-29 19:53:27Z jwage $
 */
abstract class Model_Entity_CzProject extends Doctrine_Record
{
    public function setTableDefinition()
    {
        $this->setTableName('cz_project');
        $this->hasColumn('id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => true,
             'autoincrement' => true,
             ));
        $this->hasColumn('type', 'enum', 7, array(
             'type' => 'enum',
             'length' => 7,
             'fixed' => false,
             'unsigned' => false,
             'values' => 
             array(
              0 => 'projet',
              1 => 'annonce',
             ),
             'primary' => false,
             'default' => 'annonce',
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('sousType', 'enum', 11, array(
             'type' => 'enum',
             'length' => 11,
             'fixed' => false,
             'unsigned' => false,
             'values' => 
             array(
              0 => 'proposition',
              1 => 'besoin',
             ),
             'primary' => false,
             'default' => 'proposition',
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('name', 'string', 255, array(
             'type' => 'string',
             'length' => 255,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('description', 'string', null, array(
             'type' => 'string',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('media_thumb', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'default' => '0',
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('address_id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('category', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => false,
             'autoincrement' => false,
             ));
        $this->hasColumn('goal', 'string', null, array(
             'type' => 'string',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('partners', 'string', null, array(
             'type' => 'string',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('state', 'enum', 7, array(
             'type' => 'enum',
             'length' => 7,
             'fixed' => false,
             'unsigned' => false,
             'values' => 
             array(
              0 => 'enable',
              1 => 'disable',
             ),
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('date_add', 'timestamp', null, array(
             'type' => 'timestamp',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('date_update', 'timestamp', null, array(
             'type' => 'timestamp',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'default' => '0000-00-00 00:00:00',
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('startDate', 'timestamp', null, array(
             'type' => 'timestamp',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('endDate', 'timestamp', null, array(
             'type' => 'timestamp',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('financialNeed', 'string', 255, array(
             'type' => 'string',
             'length' => 255,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('humanNeed', 'string', 255, array(
             'type' => 'string',
             'length' => 255,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('materialNeed', 'string', null, array(
             'type' => 'string',
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('creator_id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
             'notnull' => false,
             'autoincrement' => false,
             ));
    }

    public function setUp()
    {
        parent::setUp();
        $this->hasOne('Model_CzAddress as CzAddress', array(
             'local' => 'address_id',
             'foreign' => 'id'));

        $this->hasOne('Model_User as User', array(
             'local' => 'creator_id',
             'foreign' => 'id'));

        $this->hasOne('Model_CzMedia as CzMedia', array(
             'local' => 'media_thumb',
             'foreign' => 'id'));

        $this->hasOne('Model_CzCategory as CzCategory', array(
             'local' => 'category',
             'foreign' => 'id'));

        $this->hasMany('Model_CzComment as CzComment', array(
             'local' => 'id',
             'foreign' => 'project_id'));

        $this->hasMany('Model_CzProjectCategory as CzProjectCategory', array(
             'local' => 'id',
             'foreign' => 'project_id'));

        $this->hasMany('Model_CzProjectLeader as CzProjectLeader', array(
             'local' => 'id',
             'foreign' => 'project_id'));

        $this->hasMany('Model_CzProjectMaterialneed as CzProjectMaterialneed', array(
             'local' => 'id',
             'foreign' => 'project_id'));

        $this->hasMany('Model_CzProjectMedia as CzProjectMedia', array(
             'local' => 'id',
             'foreign' => 'project_id'));
    }
}