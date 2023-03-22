-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 30, 2022 at 09:33 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fruitquality`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `adminID` int(11) NOT NULL,
  `adminName` varchar(255) NOT NULL,
  `adminPass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`adminID`, `adminName`, `adminPass`) VALUES
(1, 'admin', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `fruit`
--

CREATE TABLE `fruit` (
  `fruitID` int(11) NOT NULL,
  `fruitName` varchar(255) NOT NULL,
  `fruitImage` longblob NOT NULL,
  `fruitCondition` varchar(255) NOT NULL,
  `fruitSize` varchar(255) NOT NULL,
  `fruitTexture` varchar(255) NOT NULL,
  `fruitColor` varchar(255) NOT NULL,
  `fruitSurvival` varchar(255) NOT NULL,
  `dateTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fruit`
--

INSERT INTO `fruit` (`fruitID`, `fruitName`, `fruitImage`, `fruitCondition`, `fruitSize`, `fruitTexture`, `fruitColor`, `fruitSurvival`, `dateTime`) VALUES
(12, 'Mango', 0xffd8ffe000104a46494600010100000100010000ffdb004300080606070605080707070909080a0c140d0c0b0b0c1912130f141d1a1f1e1d1a1c1c20242e2720222c231c1c2837292c30313434341f27393d38323c2e333432ffdb0043010909090c0b0c180d0d1832211c213232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232ffc000110800e000e003012200021101031101ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a161718191a25262728292a3435363738393a434445464748494a535455565758595a636465666768696a737475767778797a838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae1e2e3e4e5e6e7e8e9eaf1f2f3f4f5f6f7f8f9faffc4001f0100030101010101010101010000000000000102030405060708090a0bffc400b51100020102040403040705040400010277000102031104052131061241510761711322328108144291a1b1c109233352f0156272d10a162434e125f11718191a262728292a35363738393a434445464748494a535455565758595a636465666768696a737475767778797a82838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae2e3e4e5e6e7e8e9eaf2f3f4f5f6f7f8f9faffda000c03010002110311003f00f1da33ed451ce2ac40296928a00752d20a514809178a05341e2945003e96929c28180f7a70e94829c2810a29e29a05380a4038734e1d290669681067bd263f5a5a3bd00371cf4a5ef4629714000a28a5c50002940ed40eb4ea04005380e94829477a0070a9074a8d7d6a41f4a4073d476a39a4e6ac614b45140c5a51d29314e1d47a5210a29c291800e403900f06945031c29c29a29e066818a3ad3a905385210a074a781c52014eed400a2971476a5e82900868c52d140841d6971c518a502801314629df8d277a002814bd68a60283cd2e3a520e29c3ad02b0a318a9053053d4f3480e7e8a28ed5630a3bd14b40c302968a5a402d28a4a70a005029eb4de94f1c5218e1d29e0714d1c53c50028e94e1cd26314e02908514ec66931f9d28eb4009da8c53a819c521898a5c52d2e38a0561b8a31c5388a4ef400847bd18a5a39a620c5281cd03eb4a3340851522d30548381401cf74a5fc28a5ab284c514bda8a0402947068145218b4a281d69450316a414c029ebd690120e69c29a314f06900b4bde8029d400a294536a68ade597ee213ef49b4b72a317276488c71da97a0ab834bbb3d23cfb66a19ade680e258d94fb8a8538bd9972a3522af24c8a9c0520f6a3b559981a28a33f9d0213f0a297b514c9614a2929475eb400e14e1d7ad3475f6a703c5023068a5c515630ef40a5a281852d1d297148041c5385276a5140c753871de9a29e3a74a403853c5305385201e29c324e00e4d347735a1a7db8660edf87b54549a82bb37a145d69f2a2c5969eb80f2f27b0adc8605c0da303d2990228404025bdead0560c3fc3a579752aca4eecfa0a74614972c513c2a8ae3e5ebd2afcb656d73098e440430ace646da369e6ad432385c83b941c1c73c57349be836721abe92da7cc59016849e0fa56676aef6ee28ee6078e4e841c9ae16789a09de36e707afa8af530b5fda2e596e8f171b8754e5cd1d98cedd283ed474a2bace110f5a5a4ec68ed4122fd29692973f95310a39a70e29a3f9d3b340189452914558c28a5c518a0602968c52f7a003f5a28c52814862d387514dcd28eb48070a777a6e73c500f7a404f02192400f4ef5bd6b17238e056658c455338cb1add8232e9d3bf38af3b1153999efe0e92a71f365804ee0f9217a0c5491c84b82c78cf1eb4d41c10bd3a5584452a3a66b89b3adcac4ae49646c703f4a9edd1fcbdc4f5fe1a6463cc42adb769e3eb5722450a0038e3181daa199b0489990ee50011c8ae57c4f65f679a19800030da703b8aec517271d8f7acbf155b09b4732019319dd5a61ea72554ce7c4c39e935d4e0c1a2929457b8782c5cd0451df8a0531052d14502145380a68a5ed41263e28a5a3b5596252f7a5efcd18e2801314e028a5c0cf1d3d68000b415c528c67d294fb520198e69c2933477e290c5a9ade2323eeec2a0cd6a5bc7b2254ee7ad635a5cb13af094f9e777d0b96d1e0648e71cd6c40c625e475e954eda20c809e075ab8cc3cbe9c7ad79751dcf620ec4b1b6e7c2f43fa5584382437614cb3808cae724f39a9dc10495c6715848b931d1918c738fe5566d3ef0de6ab44497008e49c7d2afc6bb480a0543666d9704648c038e7ad57d46233584d130c06522adc793827ae31514b821948ed509d9dc8e6bab33ca718241ed4e1eb4f9c62e6503a6f3fcea315f489dd1e03dc776e9462814bdaa84276a5ef4500f3d2826e28a0519e2947a9a00c9a31cd2d0056830ea281ef4b452187340e39a3b52e31400529a4a29006283477a434863a04f36e113d4d74514072063158da5a86bf41ec6bad8a11f2f1ce79af3f173b4923d7c0457b36fcc8e357042fe06aec70820824714c48c87248efd6aec4800cb019e95e7b773a9bb0e8c00b8a539e83afad38ae1432fe54d3201df0693d85cd70b58dfcc60cd9c124715a2140db83cd538d497dc0e3deaf2f4073c8ac9b2252b1663202e3bd4174e1119bb0eb52a9e327a565f882e45b68f3c99c315d83ea78a508f34947b9939593933cea46df2bb7f7989a334d029c3a715f4a8f1d8a0734b8e68a31cd3245a3f0a28ef40829c3a629a07ad380ed4c46577a28a335450669451d2819cd002834bc9a4a5a430a28e68ed4009da90f4a5e4504e690c9f4d7d9a9424f4ce2bb74c63771cd79f2c863951c75520d75f1de16daca415619af3b1b17cca47a5819fbae26da618548a4f7cfbd6743761fe4cedab81f0bcfa715e7dec764ac4de67029ae79cf715503975201229935cf96718249f4a995d99b669c2c4b75ce7f4abd1c81718c64563d9caeea19c053e957779c6734ac4bd4bab282724d721e2fd43cc962b256cedf9dfebd856cdf6a71d8da3cafd14703d4f615c04d3c9713bcd29cbb9dc4d76e068f34f9dec8e5c454b47950e069c326a3069e0d7ac700e1c53bd29b9a506810b40a3268a0051c114b9e69296988cbc5280297140e6a861f852ff004a0fa518a004a28a3ad200a3b52e283c1140c6fd290d3bb734d3f5a4318d5a5a65e0d9e431e57eefd2b348a665958329c1078359d5a6a71b32e9cdc1dd1d325cfef476feb5792e18ff00113f8d73305f2bb2890ed71dfb1ad386e5564cf507d2bcba945c5ea8f4615d491b4b37190695a4593183820e6b3fed007dd39cf4a9e292354563807ad73b88f9d1a514843e09f94d32e6f3c906467daa9d73d2b2a7d66dedc10796f41d4d605eea135fbe5ce107441dab7a3859d4777a231a95947627d4b5393509f2722253f2aff5aaa0d422a45af5e10508f2a3864db7764c0d3c1150a9e6a5078aa2078a764714d079a5a403a969334a2810a3a74a70c534629c280b199d1a971c51d78cd2f7ab00c1a434bde97bd0037a528ce7b514742290c4a3145140c43cd34f14e23d39a4a0061a630a90f5eb4c22819111c50aee9f75d87d0d388cd2103349abee0482f6e578121a1aeee240434cd8f6a8b14e18a9e48f61dd82fbf3520e82983ad3aac43c5387d2983da9c2802553522fb544b522fb52112034f151834e140878a77434c079c53bda90870e69c3a718a68a70ed8a606763f1a318eb4a7af1d68fad50087ad2f6a3da81d2800cfe74d14eef49ef40c0f02938a5ef4defcd200a4341a4cfa9a0634d34d38fad30fd281898a434b4868012945252d021453bb53734b9c8a063a9c0d305385004ab4f53c5443ad4ab8a04c9053d6a314f1f4a448f1d69cbd2983ad3c5003853c0f7a60c0e69e314019d9ef4b9fc68fca83ed54027bd1ed4119a422801693de8391ee2939f4a005cd34d2d2503118d37ad29a6d030269869d4c3d690099cd14525002d25145002e694520a075a007e69c0d329c298c914d49512d4a2825920a78a8c7b53c52131e334e14c14f148070e29e0d340f7a70393480a38e79a4c52f14558210e3ad21eb41a4ea6800e3d68a4a09a0009ed8a6934b49eb40087a530d3cfeb4c341421a69a53486801b4514940052d26681f5a005a5a4a07d6801c29c29a0f14e5a00914d48bc8a88751522e2813255a78f4a8c53c13eb4843c7ad3853453c0f7a421579a91699e9cd3c718ef40cffd9, 'Fresh Mango', 'Size A', 'Pulpy', '85%-100% Yellow-orange', '5 Day', '2022-12-30 14:41:47'),
(13, 'Mango', 0xffd8ffe000104a46494600010100000100010000ffdb004300080606070605080707070909080a0c140d0c0b0b0c1912130f141d1a1f1e1d1a1c1c20242e2720222c231c1c2837292c30313434341f27393d38323c2e333432ffdb0043010909090c0b0c180d0d1832211c213232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232ffc000110800e000e003012200021101031101ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a161718191a25262728292a3435363738393a434445464748494a535455565758595a636465666768696a737475767778797a838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae1e2e3e4e5e6e7e8e9eaf1f2f3f4f5f6f7f8f9faffc4001f0100030101010101010101010000000000000102030405060708090a0bffc400b51100020102040403040705040400010277000102031104052131061241510761711322328108144291a1b1c109233352f0156272d10a162434e125f11718191a262728292a35363738393a434445464748494a535455565758595a636465666768696a737475767778797a82838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae2e3e4e5e6e7e8e9eaf2f3f4f5f6f7f8f9faffda000c03010002110311003f00f1da33ed451ce2ac40296928a00752d20a514809178a05341e2945003e96929c28180f7a70e94829c2810a29e29a05380a4038734e1d290669681067bd263f5a5a3bd00371cf4a5ef4629714000a28a5c50002940ed40eb4ea04005380e94829477a0070a9074a8d7d6a41f4a4073d476a39a4e6ac614b45140c5a51d29314e1d47a5210a29c291800e403900f06945031c29c29a29e066818a3ad3a905385210a074a781c52014eed400a2971476a5e82900868c52d140841d6971c518a502801314629df8d277a002814bd68a60283cd2e3a520e29c3ad02b0a318a9053053d4f3480e7e8a28ed5630a3bd14b40c302968a5a402d28a4a70a005029eb4de94f1c5218e1d29e0714d1c53c50028e94e1cd26314e02908514ec66931f9d28eb4009da8c53a819c521898a5c52d2e38a0561b8a31c5388a4ef400847bd18a5a39a620c5281cd03eb4a3340851522d30548381401cf74a5fc28a5ab284c514bda8a0402947068145218b4a281d69450316a414c029ebd690120e69c29a314f06900b4bde8029d400a294536a68ade597ee213ef49b4b72a317276488c71da97a0ab834bbb3d23cfb66a19ade680e258d94fb8a8538bd9972a3522af24c8a9c0520f6a3b559981a28a33f9d0213f0a297b514c9614a2929475eb400e14e1d7ad3475f6a703c5023068a5c515630ef40a5a281852d1d297148041c5385276a5140c753871de9a29e3a74a403853c5305385201e29c324e00e4d347735a1a7db8660edf87b54549a82bb37a145d69f2a2c5969eb80f2f27b0adc8605c0da303d2990228404025bdead0560c3fc3a579752aca4eecfa0a74614972c513c2a8ae3e5ebd2afcb656d73098e440430ace646da369e6ad432385c83b941c1c73c57349be836721abe92da7cc59016849e0fa56676aef6ee28ee6078e4e841c9ae16789a09de36e707afa8af530b5fda2e596e8f171b8754e5cd1d98cedd283ed474a2bace110f5a5a4ec68ed4122fd29692973f95310a39a70e29a3f9d3b340189452914558c28a5c518a0602968c52f7a003f5a28c52814862d387514dcd28eb48070a777a6e73c500f7a404f02192400f4ef5bd6b17238e056658c455338cb1add8232e9d3bf38af3b1153999efe0e92a71f365804ee0f9217a0c5491c84b82c78cf1eb4d41c10bd3a5584452a3a66b89b3adcac4ae49646c703f4a9edd1fcbdc4f5fe1a6463cc42adb769e3eb5722450a0038e3181daa199b0489990ee50011c8ae57c4f65f679a19800030da703b8aec517271d8f7acbf155b09b4732019319dd5a61ea72554ce7c4c39e935d4e0c1a2929457b8782c5cd0451df8a0531052d14502145380a68a5ed41263e28a5a3b5596252f7a5efcd18e2801314e028a5c0cf1d3d68000b415c528c67d294fb520198e69c2933477e290c5a9ade2323eeec2a0cd6a5bc7b2254ee7ad635a5cb13af094f9e777d0b96d1e0648e71cd6c40c625e475e954eda20c809e075ab8cc3cbe9c7ad79751dcf620ec4b1b6e7c2f43fa5584382437614cb3808cae724f39a9dc10495c6715848b931d1918c738fe5566d3ef0de6ab44497008e49c7d2afc6bb480a0543666d9704648c038e7ad57d46233584d130c06522adc793827ae31514b821948ed509d9dc8e6bab33ca718241ed4e1eb4f9c62e6503a6f3fcea315f489dd1e03dc776e9462814bdaa84276a5ef4500f3d2826e28a0519e2947a9a00c9a31cd2d0056830ea281ef4b452187340e39a3b52e31400529a4a29006283477a434863a04f36e113d4d74514072063158da5a86bf41ec6bad8a11f2f1ce79af3f173b4923d7c0457b36fcc8e357042fe06aec70820824714c48c87248efd6aec4800cb019e95e7b773a9bb0e8c00b8a539e83afad38ae1432fe54d3201df0693d85cd70b58dfcc60cd9c124715a2140db83cd538d497dc0e3deaf2f4073c8ac9b2252b1663202e3bd4174e1119bb0eb52a9e327a565f882e45b68f3c99c315d83ea78a508f34947b9939593933cea46df2bb7f7989a334d029c3a715f4a8f1d8a0734b8e68a31cd3245a3f0a28ef40829c3a629a07ad380ed4c46577a28a335450669451d2819cd002834bc9a4a5a430a28e68ed4009da90f4a5e4504e690c9f4d7d9a9424f4ce2bb74c63771cd79f2c863951c75520d75f1de16daca415619af3b1b17cca47a5819fbae26da618548a4f7cfbd6743761fe4cedab81f0bcfa715e7dec764ac4de67029ae79cf715503975201229935cf96718249f4a995d99b669c2c4b75ce7f4abd1c81718c64563d9caeea19c053e957779c6734ac4bd4bab282724d721e2fd43cc962b256cedf9dfebd856cdf6a71d8da3cafd14703d4f615c04d3c9713bcd29cbb9dc4d76e068f34f9dec8e5c454b47950e069c326a3069e0d7ac700e1c53bd29b9a506810b40a3268a0051c114b9e69296988cbc5280297140e6a861f852ff004a0fa518a004a28a3ad200a3b52e283c1140c6fd290d3bb734d3f5a4318d5a5a65e0d9e431e57eefd2b348a665958329c1078359d5a6a71b32e9cdc1dd1d325cfef476feb5792e18ff00113f8d73305f2bb2890ed71dfb1ad386e5564cf507d2bcba945c5ea8f4615d491b4b37190695a4593183820e6b3fed007dd39cf4a9e292354563807ad73b88f9d1a514843e09f94d32e6f3c906467daa9d73d2b2a7d66dedc10796f41d4d605eea135fbe5ce107441dab7a3859d4777a231a95947627d4b5393509f2722253f2aff5aaa0d422a45af5e10508f2a3864db7764c0d3c1150a9e6a5078aa2078a764714d079a5a403a969334a2810a3a74a70c534629c280b199d1a971c51d78cd2f7ab00c1a434bde97bd0037a528ce7b514742290c4a3145140c43cd34f14e23d39a4a0061a630a90f5eb4c22819111c50aee9f75d87d0d388cd2103349abee0482f6e578121a1aeee240434cd8f6a8b14e18a9e48f61dd82fbf3520e82983ad3aac43c5387d2983da9c2802553522fb544b522fb52112034f151834e140878a77434c079c53bda90870e69c3a718a68a70ed8a606763f1a318eb4a7af1d68fad50087ad2f6a3da81d2800cfe74d14eef49ef40c0f02938a5ef4defcd200a4341a4cfa9a0634d34d38fad30fd281898a434b4868012945252d021453bb53734b9c8a063a9c0d305385004ab4f53c5443ad4ab8a04c9053d6a314f1f4a448f1d69cbd2983ad3c5003853c0f7a60c0e69e314019d9ef4b9fc68fca83ed54027bd1ed4119a422801693de8391ee2939f4a005cd34d2d2503118d37ad29a6d030269869d4c3d690099cd14525002d25145002e694520a075a007e69c0d329c298c914d49512d4a2825920a78a8c7b53c52131e334e14c14f148070e29e0d340f7a70393480a38e79a4c52f14558210e3ad21eb41a4ea6800e3d68a4a09a0009ed8a6934b49eb40087a530d3cfeb4c341421a69a53486801b4514940052d26681f5a005a5a4a07d6801c29c29a0f14e5a00914d48bc8a88751522e2813255a78f4a8c53c13eb4843c7ad3853453c0f7a421579a91699e9cd3c718ef40cffd9, 'Fresh Mango', 'Size A', 'Pulpy', '85%-100% Yellow-orange', '5 Day', '2022-12-30 14:43:31'),
(14, 'Banana', 0xffd8ffe000104a46494600010100000100010000ffdb004300080606070605080707070909080a0c140d0c0b0b0c1912130f141d1a1f1e1d1a1c1c20242e2720222c231c1c2837292c30313434341f27393d38323c2e333432ffdb0043010909090c0b0c180d0d1832211c213232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232ffc000110800e000e003012200021101031101ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a161718191a25262728292a3435363738393a434445464748494a535455565758595a636465666768696a737475767778797a838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae1e2e3e4e5e6e7e8e9eaf1f2f3f4f5f6f7f8f9faffc4001f0100030101010101010101010000000000000102030405060708090a0bffc400b51100020102040403040705040400010277000102031104052131061241510761711322328108144291a1b1c109233352f0156272d10a162434e125f11718191a262728292a35363738393a434445464748494a535455565758595a636465666768696a737475767778797a82838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae2e3e4e5e6e7e8e9eaf2f3f4f5f6f7f8f9faffda000c03010002110311003f00f32539a7114d1f853aacc84e94734bce6940a7718dc526da785a7a264f3d29361a916d3e94e00d4c903bb00aa49f40335a707877559c663d3ee181e87cb22a1cd2dca516f632941f4a9a315aafe19d622196d3ae00f6427f95556b29a06c4b0c919f46522a54e2f663706858bad5d88f20d5545c55b8c1c73d28b858b49c54f193e95593ebc5598f3f5a065943b7f0a1db03d2981bb5319cfbd005790d440646734f7eb4dcf38ef4c43d07356e11f8d56418e7156a118e73cd032e438f5ab9091f422a9a1c8f4356a16e7273ef401763e17f5e2adc6fc1e7e6acf0f93dfe9532be4e48e319a405ddc411f373433718efdf26aaac87701de9cc4e4f38a00827c9dde9fceb2a75c64f6ad39c90b9cf18f5acc9064f39cd5211e680d38734c53cf14f15a198b8a7014a07352468588ee6a5b1a1638d9d82a8c93d00ef5da685e0592e82cda8b34519e444bf78fd7d2b43c29e191688b7b771e67232887f807f8d76f04478dc71ed5e5e2718d3e581d94a87591574ed1b4fd3902db5b46847f16324fe3d6b5d146381fa52c2107402ae464579ae526eecea514b62b04e391f9d2496b04e8565891d4f665c8abe08ee2a4088dd40a9d4a38dd43c0fa5dde5a1436d21ef1f4fcab93d4fc23a8e9a0ba27da211fc718e40f715eba6d41395247b531a223871f8d7453c55586faa32952848f0b0bce31f5a99783c74af4ed5fc2965a90691144339fe341d7ea3bd705aa68b79a4cbb6e23ca13f2c8bf74d7a747130a9a7539674a50d4a1bb8e2984f34a73f4f6a61ebce2ba4c863f5a6a8f5fca9ec3a503ef5004880e7ad598f1502af156231d2802ca5584c8e83a5575e0741cd4aa70319a60585723dfdea4c907079aad903e87daa40e707938a009c4841273cf6a9376475e7deaa16e8339229e1ba926810e918b706a8c8393cf6e6ad92727ad569064f1dfd6981e5eb5328a856addb44f3c89146a599c8000ee4d5b7621225b7b696e6411c31b3b9e8aa326bbff0d7844dabadd5f2869baa47d427d7deb7f42d1e1d3ac2288a2ac9b7e7603963f5ad62eb10c2f15e457c5b97bb1d11db4a825ab1a15611d79a72cd96a8267c838a644d9039ae1f23a76351260a3ad5a8ee00c56406c9c54e8e3381d475a968a369265247353a38f6ac386e430254e40ff26ae473e4e01e7d2a5dd0ec6b29f7a98107822b3926f5ab28f9a2e4b89235bab8ca7e5552e6d23b889a19e25756182ac38357e36ed52322c83047e34d7744735b46796f883c1d25a86b9d3d5a48472d17565fa7a8ae40af3c8af7792228704647ad71de26f08a5d87bcb04559fabc6380ff004f7af430f8cfb353ef31a9453f7a279b104e7fc2940c9a92589a390a3a95607041ea2900c57a499ca3d2a753f9d42060548a7a7d29816013b7f1a901f9437f5a857007e34f56e8298c9704f24f279a917d7b63f3a83386e0735229206466811203ed4fc82bdc7ae6a35049269402475a007e0939e8075a648b8c1cf1eb522a903a645365185249c5311e5295d37842dbcfd6a36c7110ddf8d7309c115db782e58ad527b89582a81c93e959e265cb4d8e946f33d14b845dc4e0e2a1b9b8181b73cfa571daa78e2d6025223bf1dc1ae764f885286f9001fad78fecaa4f64777325b9ea3e716418ea6885d875c579c5878f7cd951252a17a1aed6c354b6be40d14a09c74cd65384e1f122d34f636d1be607bd5c5208acb4948ef5652715172916618766fc1fbc491ed9a489a48e73939cae726912619eb5306566ce7b63145ee51660b92dc30c55e8e61d8d64a0e7d2a612382306a1ee51b91c99156d1eb22de6c81cd5f46c8a1333946e5ec075c1e41aab2c2633eaa6a788f18a9480c307a55dae8c149c59c2f8abc30ba844d7768805d28c903fe5a0ff001af3831947daca4303820f6af759622871fc27a5709e30f0f72da95aa60ffcb6503aff00b5fe35dd84c434fd9cbe42ab4d497344e1554d480671cd1b69cb5ea1ca2ae72719a9076c71498e3bfd69768ed408917bd3c1c37d7b546013ee2a45078fe94c078191d39fad48a06c19cf148839dbd2a755c63d3d28000303daa294e01f7153e78f51f5aaf7070a477f4a04792834e7d42582dda046c23f26a3cd5498ee738aaa91525661076774569e6776c127150e0d583164d384352958a6ee56008ad3d3b5abad3dc157240f7e6aa98e98c95328292b3438c9ad51e8da578e0b84590ab63ae7835d9d96b56b7880ac8bb8f6cf35e09865390483ed57ad758bbb56187240f53cd79f57029eb03a215d753df84a0e086a992e0835e41a6f8de68580790fd1fa576da5f8bacaf005908463efc570d4a3386e8e88cd3d8ece398139cd5a5901158f0c8922878dc107d2acc7290707ad625a66a472ed6eb5a305c8ce335871cb9356e2939eb4ac51d1c326e1935694e6b16d6e47426b5237c81571673d4812c8a19483d2a84b1f58dc0208efdeb441c8a8668f7af1d474a6d75229caceccf28f12e8674bbc32c2a7ecb29f97fd93e9588171c57ae6a3631ea16725bccbc30c67b83eb5e5b7d672e9f7b25bcc0ee53d7d47ad7ab84c47b48f2bdd19d6a7caeeb620ed4e55e99c522fddcd3c1f6aed301579cf3ed528031918fad3147249a9010070dce29889140ee00a907a67803ad40b91c83cd4a872304fb5021e48f6aab2e3049e6ac39c2f355653ce3f0fa5303c9fb1a62c3dcf35263069c315a589b80451da94c6a7a8a5e869c2905cab241b492bd2a029ed5a58a8dedc364af06a5a1a919cc95194ab8f1b2f04530a549453294f8e59216dd1b953ed533475198fbd26ae34ec749a278cef34d9156462f1f7af51d1bc4567acc2a63900931cae6bc1cae2acd95fdc69f3acb04854839c035c55f0719eb1d19d10aed68cfa23714efc55b826cf7af3ff000bf8d22d463582e885987193debb28df186539535e54a1283b48eb8c93d8db818824f7cfad6b5adc64609ae7ede607a9ad08a4c1e0d432b73a18e4cd4fd4565db4f9c0abe8f5516735485990dc4783bc0e3bd72be29d1bedf69f6885733c438c7f10f4aeca4019483dc5643c9b1de27eabd33dc55464e9c94a25c7df8f2b3c9380707ad3b3c60f7ad6f12d8a59ea2668b1e5cdce0766f4ac45618ce735ef539a9c5497538a71e57664e180a7eec8cf4aae187ad383e7a568413a3e33cf3daa50e400323f1aa8241bbad49bf00e79268026321c72335048d9c9ebf5a5049f6c76a8998e33dcd311e5c3b7a53d4d3053ab524775a7af5a60f4a507d2908906334e14dcf34e152214a8230466a26b5047cbc1a9c1e94fc52293335e2653f30a88a56cb22b2e08cd5596d0804a8c8a45a66618ea364abcc9db1d2a174e690cad14b25bca248d8ab03c115e9fe0cf172dd85b2bb6c49d0127ad7993a60d362964b795648d8ab29c822b9ebd05563e66b4ea38bf23e8e47da783906afc1374cd79ef83bc58ba9db2db5cb013af1cf7aed51f6fd2bc49c1c64e2cee8caeae6fc32e0820d6b4130651cd7376f3e46335a96f360d67b0e4ae8da56c8c573fe298ae069925c5a67cf886e00771dc56ba3e46696641342ca79dc315a45ea64972b3ca5f508f5bd412d54e3cc872a4ff007bd3f3ac67dd1318dc6194e0e7b1ad7b3856c3c557162d09df04bbe223aed3d7f4356bc5fa4fd9a71a8423314a70f8e81bd7f1af4f0f51425c9df633af1e65cc8e77ccc7d0d395bb7f2aadbf907a53b7f239efcd7a0719681c538be3deaa07ce0e4d3839238ebd2988b218fad0cebb48e05441891ffd7a7825892c0938e33401e654be94dc73cd2fa8cd6a48e1d697ab67349df34b9c8a404839e29e2a2069e1b8a42251c77a7a9f7a8875a783481138cd48066a053cd4ea690c826b40df3275f4aa4d1633c60fa56d28e29935a8913728c354b2d181247c74aa92262b6248ba8239aa52c58a432bd95e4d617493c2c4329fcebdabc2fe218b59b15cb8f340e45788c89835a1a16b1368fa824d1b1d99f98572e270fed2375b9bd2a9caecf63e838d8835a56f38dc0679ae734ad4a2d4ec63b88981c8e7dab5a17c9e6bc66bb9da99d2413640c9ab48fcd6141718217bd68dbdcaca80835284d1ca78db4597ed09ac597cb3c0b96ff680abd6fe56bfe18883a8559e11c0fe13ff00d635bd796e2fac65b72db4ba950de99aa36ba745a55a456b083e5a0fd7bd6ee7eeaee89b1e43750bdadc4904a30f1b1523e95107e71debaff1d697b1d3518d786f924c7af63fd2b8adc327b715ed51a8aa4148f3ea47964d1309093c5489260f518154fcce4f7fc6a557f43f515b105c471d41a90364e79fc6a94678eff854c8d9e09c5023cf29c38a68a5fad6a21c339a514da72f3ce2801c0f34e04d329734844a29f9a881a7034844e95613a62aa29c1ab086932916d3071561464556438a9d0e6a19441776bb94c8839fe75952c7ed5d0f518aa37b6dd644ce0f5a451cdcd1e33551c60d6c4d1039e2b3674c13401d77813c466c2f059ccffba7e99ed5ec1138655753c1e6be6b491a2915d4e194e457b3782bc42ba95824323fef50639af2f194795f3a3b28d4bab33b369191832f523afa55a4bd6081f07935443723e951b96470437ca3b7bd70dae745ceaedae0488181a92701d3eb58361746390231183deb755c32fb521332b50b34bfb09ad25e8ea47d0f635e39750bdadcc9049c346c55bf0af6fb85dadb874af33f1e69be46a297a830938c37fbc3ff00ad5df81a969387739b110bae63955c67777e9cd499392781c73cf155c31038068df83d0e48ea7d2bd6388b68eb8ce704f14f59d307249c8ee2a829233f301839193fa53b760e4e067b7a530392ef45274ef4b5a087500d203ef45003b22941c53294520240453c76a881e69e0e4f5a044ea7153466ab29e6a6435208b88d532355556c7435283d2a4a2eabfa734ec6720d5704815207f7a4333af2dfca7e07ca7a563dcc5df15d4cb18962da7bf4358373110594f5148ab98922e0d6a787b56934bd463756c293cd51b84c13554f06a670538b8b2a32717747d13a65fc77f691cc841c8fc8d4f78c563dc3b57987817c4262905accfc138e7d6bd40159e239e845787529ba73716774649ab95f4ebbfb4b615b2532467ad757633b4908ddc1f4ae2ad564b3d430aa14370bef5d3d94c7bf53512459b0e37a9ae7bc49a78d4745b8840cc8a37a63d4735bcb2645569b87f634425cb25244c95d58f0b63f390723dba7e74c6f97a1e38e6b4fc4368d61addcc182230e5940fee9e7fad64f1b7233cfbd7d141f324d1e6356760126e5c81c0e29ead96eb8fad4218e38fd2a45c6473cd5927319a5cd2502ac075079a6e696801474a33499a01a007ad3d4d460d396901283e952ab7a5440f414f071c5211650fa9a9d48aac8c454c1bdea58c9c373826a60dd2aaab71cd4a1b8041a4345a5390466a8ea10074f317a8ea2ac06e3af7a0b0248f4a433989d739aa0e315b97d0796f903e56e95933275a0636d2e5ad6e16543d0f35ec7e16d756fecd559b2e060fbfbd78b115b5e1dd624d36f530c76e7fc8ae4c550e78dd6e8de8cececcf7390238562a0b7406afdab6d51585a65fa5edb2488d90456a44d83d4d79363aee6e452e40e696662578e95461971deac8972706a6c3b9e79f1060d9a95bce07cb347863eea7ffaf5c6b9030571cf6af46f1ec21f4db793fb92e33e808ffeb579db282b8073dbdbad7b98495e923cfacad3645e9cf38a7aee38e94d182467b8a95400e00e4575181cbd14668e9563168a4a33400b45251c0e9400f069c0d460d381a064a0d48b50a9ef5229e6912585247a54aade86abab73ea6a50d4985c9d7a53c11ea2a107a0f7a9158107b0a91a64aac3079a5dc3230722a30c003fe149b88cd03b893c7e74654f5edf5ac29a32ac548c115d006c839200f5aa37f6e1d448bd40e690d3301d699c8356a44aaecb8a06767e0ff121b5b85b69dfe56e326bd5a1984a8194e411906be755628c082411d0d7a57827c5825dba75eb812748dcff0017b57998ac3dbdf89d54eadf467a4a48462ac2dca8214900d5189b1cb1e2ac1200048cd70d8dee66f8c54be8131fee32b67f1c7f5af35d9f2e7bfae2bd5751592e6dbc955df1b022407b0c75af2b955a395d4e7284f2457a98197b8e2726217bd722e9c7e9528c533af2718f4a97007381f95771cc7274947bd25680293452668cd002e68a4cd00d00381a5cd36973401203c5381ed518200a783838cd004cad5229e47355d58f7a995b3cd211329c1e33ef52671cfa5420e0d3876e707d0d20260f9ea3a0a19b23b8fc6984b019e714de4f23f114809d58018dd8f438a427aed39fa53795cfb0fca9a1831e060673e9458667dddb796db94e41eb81d2a83a75c56eb10cfb1be65ee4fa5665c41b1895ceded49a29333c8c1a5476470ca48607208ed5232d46462a6c33d4fc19e305bd8d6c6f9c0b9518563fc63fc6baff002aeaeee831658edd4f40725bfc2bc062768dd5d18ab29c820f20d7a37863c744aa5a6a270fd165ec7ebef5e76230ce3ef4363a69d5be8cf43b9ba102940c159860135e69a9b29d46728d905cf6aeafc4176ada735c248b955f979ea7b57068d26e67918fcf8cf3fe79a7818b579115ddf726e48c00df854a303079c62a30e55413c03c71528236ab0dbcaf435e91cc71fef49de9693a0ad002928a3eb40064d2d251dfad20168e71451de980f07d69c2a314a3a6734012827352a3722a05fcaa5427ae68132653f3738a9148ea4f4e0542a062a45e9d39ce2a4438b9dc2943718c741dfad30b00b904528381ebcf14580949caf40474c67151bb64a8385cd30b0fbc3e98f5f7a61e49cb7a73e94d21926ec6718a52ab921b038fc2a0f7cf1d01f5a7824e39e3f9d1602b4b6a7965e8074cd5364ad639e3be6a36895972cbc67191eb4b94a4ccc0956ade06903608e3d6a6368bee0e6acc1108b2a083ce0f3d69240e45bb692e161f2e599dd17a213c03528da725b935017030149e0707bd3b71e3183c73cf7a146db09b6f72ca92476dbed53a9cf23b71d78aa60b03d78cf1cd588d884c1fd2811fffd9, 'Fresh Banana', 'Size A', 'Squishy', '85%-100% Yellow', '5 Day', '2022-12-30 14:45:45');

-- --------------------------------------------------------

--
-- Table structure for table `userlogin`
--

CREATE TABLE `userlogin` (
  `userID` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userlogin`
--

INSERT INTO `userlogin` (`userID`, `username`, `email`, `password`) VALUES
(1, 'Lok', 'lcl010205@gmail.com', '202cb962ac59075b964b07152d234b70');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`adminID`);

--
-- Indexes for table `fruit`
--
ALTER TABLE `fruit`
  ADD PRIMARY KEY (`fruitID`);

--
-- Indexes for table `userlogin`
--
ALTER TABLE `userlogin`
  ADD PRIMARY KEY (`userID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminlogin`
--
ALTER TABLE `adminlogin`
  MODIFY `adminID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `fruit`
--
ALTER TABLE `fruit`
  MODIFY `fruitID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `userlogin`
--
ALTER TABLE `userlogin`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;