CREATE TABLE IF NOT EXISTS `temperatures` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `dateMeasured` date NOT NULL,
  `hourMeasured` int(128) NOT NULL,
  `temperature_1` double NOT NULL,
  `temperature_2` double NOT NULL,
  `temperature_3` double NOT NULL,
  `temperature_4` double NOT NULL,
  `pressure` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `pressure_sea` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `humidity` varchar(20) NOT NULL,
  `altitude` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

