/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 8.0.13 : Database - chopper
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`chopper` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `chopper`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add post',7,'add_post'),(26,'Can change post',7,'change_post'),(27,'Can delete post',7,'delete_post'),(28,'Can view post',7,'view_post'),(29,'Can add comment',8,'add_comment'),(30,'Can change comment',8,'change_comment'),(31,'Can delete comment',8,'delete_comment'),(32,'Can view comment',8,'view_comment'),(33,'Can add Tag',9,'add_tag'),(34,'Can change Tag',9,'change_tag'),(35,'Can delete Tag',9,'delete_tag'),(36,'Can view Tag',9,'view_tag'),(37,'Can add Tagged Item',10,'add_taggeditem'),(38,'Can change Tagged Item',10,'change_taggeditem'),(39,'Can delete Tagged Item',10,'delete_taggeditem'),(40,'Can view Tagged Item',10,'view_taggeditem'),(41,'Can add site',11,'add_site'),(42,'Can change site',11,'change_site'),(43,'Can delete site',11,'delete_site'),(44,'Can view site',11,'view_site');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$120000$EmiKwGNYk0Uw$J91BjflMvVcOLuNDNzemcALQpPgbWDrlyIplbU3axbs=','2019-01-20 12:43:03.163933',1,'admin','','','admin@admin.com',1,1,'2018-11-29 09:58:37.393067'),(2,'pbkdf2_sha256$120000$egONZ5zK4eCs$j7bFi0HTpSPKsZKWHxLSXCbB+tA2yktTVff8Qdx35T4=',NULL,1,'chopper','','','chopper@chopper.com',1,1,'2018-11-29 10:00:55.739358');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `blog_comment` */

DROP TABLE IF EXISTS `blog_comment`;

CREATE TABLE `blog_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `email` varchar(254) NOT NULL,
  `body` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_comment_post_id_580e96ef_fk_blog_post_id` (`post_id`),
  CONSTRAINT `blog_comment_post_id_580e96ef_fk_blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `blog_post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `blog_comment` */

insert  into `blog_comment`(`id`,`name`,`email`,`body`,`created`,`updated`,`active`,`post_id`) values (1,'上帝视角','chopper_jj@qq.com','我觉得这个人的枪法很准','2019-01-16 14:48:05.863376','2019-01-16 15:01:56.312354',0,1),(2,'菜鸟','chopper_jj@qq.com','这是个牛逼新闻，我看看不说话','2019-01-16 14:48:12.815399','2019-01-16 14:48:12.815399',1,1),(3,'辣鸡','chopper_jj@qq.com','This is a interesting news!','2019-01-16 14:48:16.932481','2019-01-16 14:49:23.300911',1,1),(4,'Alex','chopper_jj@qq.com','I don\'t think that\'s a good news.','2019-01-20 12:50:54.307022','2019-01-20 12:50:54.307022',1,5);

/*Table structure for table `blog_post` */

DROP TABLE IF EXISTS `blog_post`;

CREATE TABLE `blog_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(250) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `body` longtext NOT NULL,
  `publish` datetime(6) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `status` varchar(10) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_post_author_id_dd7a8485_fk_auth_user_id` (`author_id`),
  KEY `blog_post_slug_b95473f2` (`slug`),
  CONSTRAINT `blog_post_author_id_dd7a8485_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

/*Data for the table `blog_post` */

insert  into `blog_post`(`id`,`title`,`slug`,`body`,`publish`,`created`,`updated`,`status`,`author_id`) values (1,'What\'s the horrible level of modern weapons have developed?','whats-horrible-level-modern-weapons-have-developed','德克萨斯州的一位农场主，利用高倍镜，夜视仪，以及一把狙击步枪，远距离干掉了入侵自己农场的45只野狼，是的，45只在视频冰冷的画面中，生命的脆弱一览无遗\r\n\r\n或许更悲哀的是，那些狼到死都不知道死神在哪里\r\n\r\n相比之下，在阿富汗或伊拉克战场上，把狼换成人，结果应该也不会差太多吧。','2018-11-29 10:01:17.000000','2018-11-29 10:03:39.237771','2019-01-03 15:20:08.356987','published',2),(2,'How to recognize the brilliant besides?','how-recognize-brilliant-besides','1.聪明人从来不多说话，那些賊喜欢发表观点侃侃而谈秀智商的，甚至为了捍卫观点争吵的面红耳赤的人，往往都是段位比较低的选手。大佬很少大声讲话，整个人显得从容淡定。更多时候在听和判断，而不是叭叭讲。对于他们来说，脑子比嘴重要。\r\n\r\n 2.待人非常随和，不随便给自己树立敌人，但是对于他的底，他又不会轻易亮给你。\r\n\r\n3.忍耐力极强。对于让他不舒服或者损害到他利益的人，并不表现出恼怒，不会为小事儿和小人物生气。很能坐得住，别人可能使劲儿一周一个月看不到前景就放弃了，但是他们会忍着，很耐心的走，定力很强。\r\n\r\n4.学习能力很快，抓重点能力极强，脑子非常灵活，再怎么有social 技巧，没有硬本事也是很难搞起一波事业。他们对于一个东西思考深度很深，同时考虑的面很广。对于一些新的东西，可能一两天就可以搞懂。\r\n\r\n5.能够保持比较长时间的专注。承接上面来讲，大部分人智商存在差别，但是差别没有现实处境这么大。那些大佬做事情非常专注，现在大部分人越活越浮躁，一点儿机会就刷手机开小差，很难做到那种旁若无人的投入。这其实就已经不是智商问题了，他们的聪明实际上是和心静联系在一起的。6.冷静到炸裂。我觉得常人经常心态爆炸，遇到紧急情况心态特别容易崩，但是那些大佬很少见到他们表现出某种常人可以见到的焦虑。实习的时候，带我的一个小哥哥，北大本硕博，一路升的很快，他经常告诉我，情绪解决不了任何问题。我真觉得他可以到很好的位置。','2018-11-29 10:03:39.000000','2018-11-29 10:04:33.884245','2019-01-20 12:45:03.327721','published',2),(3,'What\'s the old-year programmer\'s career?','whats-old-year-programmers-career','每隔一段时间总会冒出这种问题，怒答之！我今年33岁，创业失败，然后网站上投简历，按网上的说法，我这种即将35岁的人是会被歧视的，那为嘛阿里没歧视我，京东没歧视我，美团没歧视我，货车帮没歧视我，知道创宇没歧视我，够用云没歧视我，中国电信研发中心没歧视我，更不用说其他一些规模相对小的公司了，都给了面试机会，而且收到了不少的offer，最终决定加入某知名电商平台。如果我的经历没有说服力，可以去看看【中通人的一天】吉日嘎拉：中天背后的“程序猿”，也可以去网上看下阿里前端专家阮一峰，这两位大佬不都是中年以后才去了现在的公司，而且也都40了吧，不也干得热火朝天的。\r\n\r\n如果到了30多岁，知识和经验没有系统化，代码重构和架构不会，不能让写出的程序更优雅、性能更好，不知道各种框架的适用场景和优缺点、不知道一些解决方案背后的原理，技术水平也跟工作二三年的人水平差不多，请问你是老板，你会不会要自己这样的员工？不要把年龄做为停止学习的借口，年纪大了，家庭琐事多了，学习时间的确少了，但是也不可能完全没有学习时间。新事物是基于现有问题产生的解决方案，比如你是前端工程师，以前你项目迭代到一定规模，你会为UI层不能实现组件化标签调用而困扰、会被数据与DOM的关系所烦恼，会被嵌套的回调函数搞疯，所以有了react，有了es6，有了webpack，你会觉得这些技术的出现简直是水道渠成，学会了react，再学vue，可以举一反三，这些技术只需要你投入几十个小时来学习，就可以上手并在工作中带给你巨大的便利，你还要找借口，除了懒、不思进取外，我实在不知道说什么。至于发展路线，不想做技术了，如果具备转岗的一些潜力和能力，都会给转岗机会，当然薪资会降，因为你在新岗位上的经验不像你在老岗位上那么丰富，凭什么按老岗位的工资水平来付你新岗位的薪酬？','2018-11-29 10:04:33.000000','2018-11-29 10:05:46.865598','2019-01-20 12:45:20.654449','draft',1),(4,'\"DON\'T DO IT\" in the America!','dont-do-it-america','1、把鞋子放在门外——会遭来杀身之祸\r\n\r\n咱们在中国会觉得有时候比如鞋子脏放在门外，或着出去跑了一天出了汗，要把鞋子放在外面晾一下。然而，后来才听说，鞋子放在门外可能会有生命危险。\r\n\r\n因为，只有亚洲人（包括中国、日本、韩国、东南亚、印度）喜欢把鞋子放在门外。而亚洲人在美国还有几个特点：1) 体格比白人黑人瘦弱，容易欺负2) 喜欢用现金（美国可是没有地方收微信支付宝哦）3) 往往家里没有枪这就导致门口摆放鞋子的亚洲人变成了暴力犯罪分子的重点攻击对象，尤其是家里开餐馆的的亚洲人，更是容易被犯罪分子这样盯上。当然也分区域，如果住在白人、黑人较多的地方，一定要注意鞋子的摆放。而比如像我在硅谷这附近，小区里面全都是码农，除了印度人就是中国人，把鞋子放在门外的就比较多，这样情况下就问题不大了。\r\n\r\n2.在阳台上晾衣服\r\n\r\n一定觉得我是在开玩笑对么？晾衣服都不行，难道洗了衣服难道就捂着？衣服不是都要捂臭了？尤其是上海的特色风景线——万国旗，到了美国就不能盛开么？\r\n\r\n开始我也不能理解，阳台上为什么没有晾衣绳、晾衣架？本来还想自己扯一个，但是被房东劝阻了，房东是个白人老爷爷，我也没有问他理由，心里想，可能是觉得这样不礼貌？后来，在美国生活一段时间后，总结了一下几个不能在阳台上晾衣服的原因：1) 美观问题2) 美国电费很便宜，用烘干机一个月也不到7美元，美国人都用烘干机。3) 美国人房子大，没有必要晾到屋外4) 花粉过敏，美国人很多都过敏，晒在外面的衣物容易沾上花粉5) 美国人不能理解“晒”的意思，曾经跟美国朋友解释这个概念，他想了半天说“So you mean sunshine can kill bacteria?”另外一点，从自我保护的角度，就像上面说的，放鞋子和衣服在屋外都会被人发现是亚洲人，也不太安全。','2018-11-29 10:05:46.000000','2018-11-29 10:13:38.271282','2019-01-20 12:45:30.220854','draft',1),(5,'Does it\'s necessary to complete all AI algorithm by Myself?','does-its-necessary-complete-all-ai-algorithm-myself','这个经历对我的帮助大概有以下几个方面:\r\n\r\n1) 对算法细节的理解更加深刻了。书中毕竟不会给出所有细节，而且书本身可能就是错的。为了写出代码，我几乎是把所有公式重新推了一遍，自己存下的note里面公式数量绝对远远多于书本身，期间也发现了书中无数的错误，这些错误在初读的时候根本意识不到。这样一遍下来，让我对推公式的信心大增，看论文不会怕看不懂公式了。遇到看不懂的就推一遍，推不出的就抄一遍，之后总会懂的。一个side effect就是让我变得愤青了，看什么paper都觉得烂。因为读paper的时候，你会发现，很多paper违背基本常识，即使影响力非常大的一些paper里也有这样那样的错误。\r\n\r\n2) 可以了解很多看书学不到的各种trick。所有算法几乎都有坑。比如hyper-parameter什么意义怎么设，怎么初始化，numerical stability的怎么保证，如何保证矩阵正定，计算机rounding error的影响，numerical underflow和overflow问题等等。3) 对整个领域各个算法的关联有更深刻的了解，思维形成一个关系网。看到一个算法就会自然的去想跟其他算法的联系，怎么去扩展。如果一篇paper我不能把它纳入到这个关系网里，我就觉得自己没懂。要么推出联系，要么推出矛盾证明这篇paper垃圾。另一个side effect就是我看paper从来不根据实验好坏判断优劣。虽然自己动手实现算法有好处，但是性价比几何还是个见仁见智的问题，毕竟这是一个很费时的过程。我并不认为一定有必要自己实现书上所有算法，毕竟每个人所能关注的领域还是有限的，懂得算法大致原理，具体用的时候在细研究就可以。很多算法我也是写完了从来没用过。几年过去后，我在回头看自己的代码也很难看的懂，细节还得看公式。但是对于自己的研究领域我建议还是有必要把经典算法动手实现一遍加深理解。','2018-11-29 10:13:38.000000','2018-11-29 10:14:55.126743','2019-01-20 12:45:10.053144','draft',2),(6,'Does the physical store has been dead?','does-physical-store-has-been-dead','\"淘宝冲击了实体店的生意，京东抢了电器卖场的业绩\"，很多商家一边开着店一边打着骂马云，骂刘强东的口号，这成了中国的一大特色！\r\n\r\n难道实体店已死？就目前情况来看，实体店不可能会消亡，将会更好，因为实体店给消费者带来的体验，是电商无论如何也做不到的。\r\n\r\n所以传统的运营模式已经不适应现如今的市场。要根据市场的发展动态，对运营模式做出调整，转变成跨行复合、多元化、智能的运营模式！\r\n在实体店难做的今天，日本实体店依然屹立不倒，人满为患，一起来看看他们是如何做的!\r\n\r\n1.暖心的细节\r\n\r\n在日本的商场，婴儿车和轮椅，就在入口附近，旁边还放着消毒纸巾，让人感到非常暖心。\r\n在餐厅就餐，即使是忙碌的饭点，服务员也能把桌子上的餐巾纸及时补齐，并且摆放整齐。\r\n倘若看到酱油瓶、椅子偏离了原来的位置，也会及时复原，他们居然做到了如此细致。\r\n在下雨天，服务员会从顾客需求的角度出发，分别准备擦拭雨具与身体的毛巾，贴心又可再利用。\r\n女厕所，镜前是化妆台，意在分流人群，避免有人洗完手继续化妆造成排队。\r\n带婴儿的妈妈厕所。','2018-11-29 10:14:55.000000','2018-11-29 10:18:37.976301','2019-01-03 15:20:23.792557','published',1),(7,'Who was Django Reinhardt?','who-was-django-reinhardt','who was Django Reinhardt?','2018-12-20 08:22:00.000000','2018-12-20 08:23:21.128909','2019-01-03 15:20:31.419703','published',1),(8,'New title','another slug','Post body','2019-01-26 03:39:26.117257','2019-01-26 03:40:40.413471','2019-01-26 03:53:50.427789','draft',1);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (1,'2018-11-29 10:03:39.238767','1','现代武器已经发展到了多么恐怖的水平？',1,'[{\"added\": {}}]',7,1),(2,'2018-11-29 10:04:33.886739','2','如何辨认身边的聪明人？',1,'[{\"added\": {}}]',7,1),(3,'2018-11-29 10:05:46.867094','3','程序员年龄增大后的职业出路是什么？',1,'[{\"added\": {}}]',7,1),(4,'2018-11-29 10:13:38.272780','4','在美国千万别做什么?',1,'[{\"added\": {}}]',7,1),(5,'2018-11-29 10:14:55.127741','5','有没有必要把机器学习算法自己实现一遍？',1,'[{\"added\": {}}]',7,1),(6,'2018-11-29 10:18:37.977301','6','实体店已死？看日本实体店是如何“干掉”电商的！',1,'[{\"added\": {}}]',7,1),(7,'2018-12-20 08:23:21.130908','7','Who was Django Reinhardt?',1,'[{\"added\": {}}]',7,1),(8,'2018-12-25 03:33:23.119832','6','Does the physical store has been dead?',2,'[{\"changed\": {\"fields\": [\"title\", \"slug\"]}}]',7,1),(9,'2018-12-25 03:36:33.011378','5','Does it\'s necessary to complete all AI algorithm by Myself?',2,'[{\"changed\": {\"fields\": [\"title\", \"slug\"]}}]',7,1),(10,'2018-12-25 03:37:25.496868','4','\"DON\'T DO IT\" in the America!',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',7,1),(11,'2018-12-25 03:37:40.273934','4','\"DON\'T DO IT\" in the America!',2,'[{\"changed\": {\"fields\": [\"slug\"]}}]',7,1),(12,'2018-12-25 03:39:28.037622','3','What\'s the old-year programmer\'s career?',2,'[{\"changed\": {\"fields\": [\"title\", \"slug\"]}}]',7,1),(13,'2018-12-25 03:41:34.485802','2','How to recognize the brilliant besides?',2,'[{\"changed\": {\"fields\": [\"title\", \"slug\"]}}]',7,1),(14,'2018-12-25 03:44:59.525378','1','What\'s the horrible level of modern weapons have developed?',2,'[{\"changed\": {\"fields\": [\"title\", \"slug\"]}}]',7,1),(15,'2019-01-03 15:20:08.358982','1','What\'s the horrible level of modern weapons have developed?',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',7,1),(16,'2019-01-03 15:20:16.902840','2','How to recognize the brilliant besides?',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',7,1),(17,'2019-01-03 15:20:23.793554','6','Does the physical store has been dead?',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',7,1),(18,'2019-01-03 15:20:31.420702','7','Who was Django Reinhardt?',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',7,1),(19,'2019-01-16 14:48:55.858745','1','Comment by 上帝视角 on Post object (1)',2,'[{\"changed\": {\"fields\": [\"name\", \"body\"]}}]',8,1),(20,'2019-01-16 14:49:23.301883','3','Comment by 辣鸡 on Post object (1)',2,'[{\"changed\": {\"fields\": [\"name\", \"body\"]}}]',8,1),(21,'2019-01-16 15:01:56.313328','1','Comment by 上帝视角 on Post object (1)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',8,1),(22,'2019-01-16 15:03:20.776611','4','Post object (4)',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',7,1),(23,'2019-01-20 12:44:24.161142','2','Post object (2)',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',7,1),(24,'2019-01-20 12:45:03.331710','2','Post object (2)',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',7,1),(25,'2019-01-20 12:45:10.060125','5','Post object (5)',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',7,1),(26,'2019-01-20 12:45:20.662399','3','Post object (3)',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',7,1),(27,'2019-01-20 12:45:30.230826','4','Post object (4)',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',7,1),(28,'2019-01-20 12:50:54.314004','4','Comment by Alex on Post object (5)',1,'[{\"added\": {}}]',8,1),(29,'2019-01-29 14:31:12.108883','1','localhost:8000',2,'[{\"changed\": {\"fields\": [\"domain\", \"name\"]}}]',11,1);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'blog','comment'),(7,'blog','post'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(11,'sites','site'),(9,'taggit','tag'),(10,'taggit','taggeditem');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2018-11-29 09:36:06.096037'),(2,'auth','0001_initial','2018-11-29 09:36:07.236366'),(3,'admin','0001_initial','2018-11-29 09:36:07.516334'),(4,'admin','0002_logentry_remove_auto_add','2018-11-29 09:36:07.538791'),(5,'admin','0003_logentry_add_action_flag_choices','2018-11-29 09:36:07.561749'),(6,'contenttypes','0002_remove_content_type_name','2018-11-29 09:36:07.779832'),(7,'auth','0002_alter_permission_name_max_length','2018-11-29 09:36:07.896611'),(8,'auth','0003_alter_user_email_max_length','2018-11-29 09:36:08.088247'),(9,'auth','0004_alter_user_username_opts','2018-11-29 09:36:08.117691'),(10,'auth','0005_alter_user_last_login_null','2018-11-29 09:36:08.231973'),(11,'auth','0006_require_contenttypes_0002','2018-11-29 09:36:08.247443'),(12,'auth','0007_alter_validators_add_error_messages','2018-11-29 09:36:08.274891'),(13,'auth','0008_alter_user_username_max_length','2018-11-29 09:36:08.411631'),(14,'auth','0009_alter_user_last_name_max_length','2018-11-29 09:36:08.558851'),(15,'blog','0001_initial','2018-11-29 09:36:08.765957'),(16,'sessions','0001_initial','2018-11-29 09:36:08.846304'),(17,'taggit','0001_initial','2019-01-16 14:43:08.165707'),(18,'taggit','0002_auto_20150616_2121','2019-01-16 14:43:08.244003'),(19,'blog','0002_comment','2019-01-16 14:43:08.522462'),(20,'blog','0003_post_tags','2019-01-16 14:43:08.545401'),(21,'sites','0001_initial','2019-01-29 14:11:39.630162'),(22,'sites','0002_alter_domain_unique','2019-01-29 14:11:39.670054');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('75grkpp42dlajxoby7luuv526mh2dexn','ZDM3ZDQwYjVjYjZlZjI5NzczOGE3MWNhYjI2NDY5ZWRlY2ViMWFmZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNmI1ZDBmMTJhMjhlNTU0ZjZjMWNjY2IxMzk5NDRiMjE3MzAwNmQ5In0=','2019-01-03 08:21:57.655070'),('i20vaojq5bw8vh32vcfgnvvmr17vpghr','ZDM3ZDQwYjVjYjZlZjI5NzczOGE3MWNhYjI2NDY5ZWRlY2ViMWFmZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNmI1ZDBmMTJhMjhlNTU0ZjZjMWNjY2IxMzk5NDRiMjE3MzAwNmQ5In0=','2019-01-08 03:28:38.279613'),('wtqqmehh8refzgtdq6igq513lheqahoc','ZDM3ZDQwYjVjYjZlZjI5NzczOGE3MWNhYjI2NDY5ZWRlY2ViMWFmZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNmI1ZDBmMTJhMjhlNTU0ZjZjMWNjY2IxMzk5NDRiMjE3MzAwNmQ5In0=','2018-12-13 09:59:16.691349'),('z8t43xid6nu5e3b75ftfygba2d6f6eaw','ZDM3ZDQwYjVjYjZlZjI5NzczOGE3MWNhYjI2NDY5ZWRlY2ViMWFmZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNmI1ZDBmMTJhMjhlNTU0ZjZjMWNjY2IxMzk5NDRiMjE3MzAwNmQ5In0=','2019-02-03 12:43:03.179891'),('zzhyux4zzyfh4b0wi0i5bczso04v79dc','ZDM3ZDQwYjVjYjZlZjI5NzczOGE3MWNhYjI2NDY5ZWRlY2ViMWFmZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNmI1ZDBmMTJhMjhlNTU0ZjZjMWNjY2IxMzk5NDRiMjE3MzAwNmQ5In0=','2019-01-17 15:04:23.579104');

/*Table structure for table `django_site` */

DROP TABLE IF EXISTS `django_site`;

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `django_site` */

insert  into `django_site`(`id`,`domain`,`name`) values (1,'localhost:8000','localhost:8000');

/*Table structure for table `taggit_tag` */

DROP TABLE IF EXISTS `taggit_tag`;

CREATE TABLE `taggit_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `taggit_tag` */

insert  into `taggit_tag`(`id`,`name`,`slug`) values (1,'music','music'),(2,'django','django'),(3,'jazz','jazz'),(4,'education','education');

/*Table structure for table `taggit_taggeditem` */

DROP TABLE IF EXISTS `taggit_taggeditem`;

CREATE TABLE `taggit_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` (`tag_id`),
  KEY `taggit_taggeditem_object_id_e2d7d1df` (`object_id`),
  KEY `taggit_taggeditem_content_type_id_object_id_196cc965_idx` (`content_type_id`,`object_id`),
  CONSTRAINT `taggit_taggeditem_content_type_id_9957a03c_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `taggit_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

/*Data for the table `taggit_taggeditem` */

insert  into `taggit_taggeditem`(`id`,`object_id`,`content_type_id`,`tag_id`) values (1,1,7,1),(3,1,7,3),(4,4,7,1),(5,2,7,4),(6,5,7,4),(7,3,7,2),(8,4,7,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
