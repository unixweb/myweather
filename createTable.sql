CREATE TABLE IF NOT EXISTS `temperatures` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `humidity` varchar(20) NOT NULL,
  `dateMeasured` date NOT NULL,
  `hourMeasured` int(128) NOT NULL,
  `temperature-1` double NOT NULL,
  `temperature-2` double NOT NULL,
  `temperature-3` double NOT NULL,
  `temperature-4` double NOT NULL,
  `pressure` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `pressure-sea` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `altitude` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
