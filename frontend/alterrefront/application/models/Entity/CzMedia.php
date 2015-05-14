<?php
// Connection Component Binding
Doctrine_Manager::getInstance()->bindComponent('Model_CzMedia', 'doctrine');

/**
 * Model_Entity_CzMedia
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @property integer $id
 * @property string $link
 * @property string $name
 * @property enum $format
 * @property enum $type
 * @property timestamp $date
 * @property enum $state
 * @property Doctrine_Collection $CzCategory
 * @property Doctrine_Collection $CzCategory_3
 * @property Doctrine_Collection $CzProject
 * @property Doctrine_Collection $CzProjectMedia
 * @property Doctrine_Collection $CzUserMedia
 * @property Doctrine_Collection $User
 * 
 * @package    ##PACKAGE##
 * @subpackage ##SUBPACKAGE##
 * @author     ##NAME## <##EMAIL##>
 * @version    SVN: $Id: Builder.php 7490 2010-03-29 19:53:27Z jwage $
 */
abstract class Model_Entity_CzMedia extends Doctrine_Record
{
    public function setTableDefinition()
    {
        $this->setTableName('cz_media');
        $this->hasColumn('id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => true,
             'autoincrement' => true,
             ));
        $this->hasColumn('link', 'string', 255, array(
             'type' => 'string',
             'length' => 255,
             'fixed' => false,
             'unsigned' => false,
             'primary' => false,
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
        $this->hasColumn('format', 'enum', 11, array(
             'type' => 'enum',
             'length' => 11,
             'fixed' => false,
             'unsigned' => false,
             'values' => 
             array(
              0 => 'movie',
              1 => 'picture',
              2 => 'application',
             ),
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('type', 'enum', 7, array(
             'type' => 'enum',
             'length' => 7,
             'fixed' => false,
             'unsigned' => false,
             'values' => 
             array(
              0 => 'user',
              1 => 'ad',
              2 => 'project',
             ),
             'primary' => false,
             'notnull' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('date', 'timestamp', null, array(
             'type' => 'timestamp',
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
             'default' => 'enable',
             'notnull' => true,
             'autoincrement' => false,
             ));
    }

    public function setUp()
    {
        parent::setUp();
        $this->hasMany('Model_CzCategory as CzCategory', array(
             'local' => 'id',
             'foreign' => 'picto'));

        $this->hasMany('Model_CzCategory as CzCategory_3', array(
             'local' => 'id',
             'foreign' => 'image'));

        $this->hasMany('Model_CzProject as CzProject', array(
             'local' => 'id',
             'foreign' => 'media_thumb'));

        $this->hasMany('Model_CzProjectMedia as CzProjectMedia', array(
             'local' => 'id',
             'foreign' => 'media_id'));

        $this->hasMany('Model_CzUserMedia as CzUserMedia', array(
             'local' => 'id',
             'foreign' => 'media_id'));

        $this->hasMany('Model_User as User', array(
             'local' => 'id',
             'foreign' => 'media_id'));
    }
}