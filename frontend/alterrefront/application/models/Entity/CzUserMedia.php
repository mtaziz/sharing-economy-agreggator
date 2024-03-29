<?php
// Connection Component Binding
Doctrine_Manager::getInstance()->bindComponent('Model_CzUserMedia', 'doctrine');

/**
 * Model_Entity_CzUserMedia
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @property integer $user_id
 * @property integer $media_id
 * @property enum $state
 * @property timestamp $date
 * @property Model_User $User
 * @property Model_CzMedia $CzMedia
 * 
 * @package    ##PACKAGE##
 * @subpackage ##SUBPACKAGE##
 * @author     ##NAME## <##EMAIL##>
 * @version    SVN: $Id: Builder.php 7490 2010-03-29 19:53:27Z jwage $
 */
abstract class Model_Entity_CzUserMedia extends Doctrine_Record
{
    public function setTableDefinition()
    {
        $this->setTableName('cz_user_media');
        $this->hasColumn('user_id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => true,
             'autoincrement' => false,
             ));
        $this->hasColumn('media_id', 'integer', 4, array(
             'type' => 'integer',
             'length' => 4,
             'fixed' => false,
             'unsigned' => false,
             'primary' => true,
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
        $this->hasColumn('date', 'timestamp', null, array(
             'type' => 'timestamp',
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
        $this->hasOne('Model_User as User', array(
             'local' => 'user_id',
             'foreign' => 'id'));

        $this->hasOne('Model_CzMedia as CzMedia', array(
             'local' => 'media_id',
             'foreign' => 'id'));
    }
}