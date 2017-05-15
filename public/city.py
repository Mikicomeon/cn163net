# -*- coding: utf-8 -*-

from collections import OrderedDict


class City:
    city_list = OrderedDict(
            [
                (u'三亚', 345),
                (u'长沙', 344),
                (u'丽江', 279),
                (u'昆明', 267),
                (u'贵阳', 258),
                (u'东莞', 219),
                (u'佛山', 208),
                (u'珠海', 206),
                (u'郑州', 160),
                (u'威海', 152),
                (u'烟台', 148),
                (u'南昌', 134),
                (u'合肥', 110),
                (u'台州', 108),
                (u'绍兴', 104),
                (u'嘉兴', 102),
                (u'温州', 101),
                (u'南通', 94),
                (u'常州', 93),
                (u'哈尔滨', 79),
                (u'长春', 70),
                (u'太原', 35),
                (u'石家庄', 24),
                (u'海口', 23),
                (u'济南', 22),
                (u'青岛', 21),
                (u'大连', 19),
                (u'沈阳', 18),
                (u'西安', 17),
                (u'武汉', 16),
                (u'厦门', 15),
                (u'福州', 14),
                (u'无锡', 13),
                (u'宁波', 11),
                (u'天津', 10),
                (u'重庆', 9),
                (u'成都', 8),
                (u'深圳', 7),
                (u'苏州', 6),
                (u'南京', 5),
                (u'广州', 4),
                (u'杭州', 3),
                (u'北京', 2),
                (u'上海', 1)
            ]
    )
    city_list_bak = {
        u'沈阳': 18,
        u'青岛': 21,
        u'成都': 8,
        u'西安': 17,
        u'大连': 19,
        u'重庆': 9,
        u'北京': 2,
        u'天津': 10,
        u'上海': 1,
        u'杭州': 3,
        u'宁波': 11,
        u'广州': 4,
        u'深圳': 7,
        u'南京': 5,
        u'苏州': 6,
        u'武汉': 16,
        u'厦门': 15,
        u'长沙': 344,
        u'三亚': 345,
        u'南通': 94,
        u'南昌': 134,
        u'烟台': 148,
        u'哈尔滨': 79,
        u'长春': 70,
        u'珠海': 206,
        u'佛山': 208,
        u'济南': 22,
        u'石家庄': 24,
        u'海口': 23,
        u'威海': 152,
        u'温州': 101,
        u'台州': 108,
        u'昆明': 267,
        u'丽江': 279,
        u'无锡': 13,
        u'绍兴': 104,
        u'嘉兴': 102,
        u'贵阳': 258,
        u'太原': 35,
        u'郑州': 160,
        u'合肥': 110,
        u'东莞': 219,
        u'福州': 14,
        u'常州': 93
    }
    city_hotel_pingyin_bak = [(u'北京', 'http://www.dianping.com/beijing/hotel'),
                              (u'天津', 'http://www.dianping.com/tianjin/hotel'),
                              (u'沈阳', 'http://www.dianping.com/shenyang/hotel'),
                              (u'大连', 'http://www.dianping.com/dalian/hotel'),
                              (u'长春', 'http://www.dianping.com/changchun/hotel'),
                              (u'哈尔滨', 'http://www.dianping.com/haerbin/hotel'),
                              (u'石家庄', 'http://www.dianping.com/shijiazhuang/hotel'),
                              (u'太原', 'http://www.dianping.com/taiyuan/hotel'),
                              (u'呼和浩特', 'http://www.dianping.com/huhehaote/hotel'),
                              (u'廊坊', 'http://www.dianping.com/langfang/hotel'),
                              (u'上海', 'http://www.dianping.com/shanghai/hotel'),
                              (u'杭州', 'http://www.dianping.com/hangzhou/hotel'),
                              (u'南京', 'http://www.dianping.com/nanjing/hotel'),
                              (u'苏州', 'http://www.dianping.com/suzhou/hotel'),
                              (u'无锡', 'http://www.dianping.com/wuxi/hotel'),
                              (u'济南', 'http://www.dianping.com/jinan/hotel'),
                              (u'厦门', 'http://www.dianping.com/xiamen/hotel'),
                              (u'宁波', 'http://www.dianping.com/ningbo/hotel'),
                              (u'福州', 'http://www.dianping.com/fuzhou/hotel'),
                              (u'青岛', 'http://www.dianping.com/qingdao/hotel'),
                              (u'合肥', 'http://www.dianping.com/hefei/hotel'),
                              (u'常州', 'http://www.dianping.com/changzhou/hotel'),
                              (u'扬州', 'http://www.dianping.com/yangzhou/hotel'),
                              (u'温州', 'http://www.dianping.com/wenzhou/hotel'),
                              (u'绍兴', 'http://www.dianping.com/shaoxing/hotel'),
                              (u'嘉兴', 'http://www.dianping.com/jiaxing/hotel'),
                              (u'烟台', 'http://www.dianping.com/yantai/hotel'),
                              (u'威海', 'http://www.dianping.com/weihai/hotel'),
                              (u'镇江', 'http://www.dianping.com/zhenjiang/hotel'),
                              (u'南通', 'http://www.dianping.com/nantong/hotel'),
                              (u'金华', 'http://www.dianping.com/jinhua/hotel'),
                              (u'徐州', 'http://www.dianping.com/xuzhou/hotel'),
                              (u'潍坊', 'http://www.dianping.com/weifang/hotel'),
                              (u'淄博', 'http://www.dianping.com/zibo/hotel'),
                              (u'临沂', 'http://www.dianping.com/linyi/hotel'),
                              (u'马鞍山', 'http://www.dianping.com/maanshan/hotel'),
                              (u'台州', 'http://www.dianping.com/zhejiangtaizhou/hotel'),
                              (u'泰州', 'http://www.dianping.com/taizhou/hotel'),
                              (u'济宁', 'http://www.dianping.com/jining/hotel'),
                              (u'泰安', 'http://www.dianping.com/taian/hotel'),
                              (u'成都', 'http://www.dianping.com/chengdu/hotel'),
                              (u'武汉', 'http://www.dianping.com/wuhan/hotel'),
                              (u'郑州', 'http://www.dianping.com/zhengzhou/hotel'),
                              (u'长沙', 'http://www.dianping.com/changsha/hotel'),
                              (u'南昌', 'http://www.dianping.com/nanchang/hotel'),
                              (u'贵阳', 'http://www.dianping.com/guiyang/hotel'),
                              (u'西宁', 'http://www.dianping.com/xining/hotel'),
                              (u'重庆', 'http://www.dianping.com/chongqing/hotel'),
                              (u'西安', 'http://www.dianping.com/xian/hotel'),
                              (u'昆明', 'http://www.dianping.com/kunming/hotel'),
                              (u'兰州', 'http://www.dianping.com/lanzhou/hotel'),
                              (u'乌鲁木齐', 'http://www.dianping.com/wulumuqi/hotel'),
                              (u'银川', 'http://www.dianping.com/yinchuan/hotel'),
                              (u'广州', 'http://www.dianping.com/guangzhou/hotel'),
                              (u'深圳', 'http://www.dianping.com/shenzhen/hotel'),
                              (u'佛山', 'http://www.dianping.com/foshan/hotel'),
                              (u'珠海', 'http://www.dianping.com/zhuhai/hotel'),
                              (u'东莞', 'http://www.dianping.com/dongguan/hotel'),
                              (u'三亚', 'http://www.dianping.com/sanya/hotel'),
                              (u'海口', 'http://www.dianping.com/haikou/hotel'),
                              (u'南宁', 'http://www.dianping.com/nanning/hotel'),
                              (u'惠州', 'http://www.dianping.com/huizhou/hotel'),
                              (u'香港', 'http://www.dianping.com/hongkong/hotel'),
                              (u'澳门', 'http://www.dianping.com/macau/hotel'),
                              (u'台北', 'http://www.dianping.com/taipei/hotel'),
                              (u'高雄', 'http://www.dianping.com/kaohsiung/hotel'),
                              (u'垦丁', 'http://www.dianping.com/kenting/hotel'),
                              (u'花莲', 'http://www.dianping.com/hualien/hotel'),
                              (u'东京', 'http://www.dianping.com/tokyo/hotel'),
                              (u'首尔', 'http://www.dianping.com/seoul/hotel'),
                              (u'曼谷', 'http://www.dianping.com/bangkok/hotel'),
                              (u'新加坡', 'http://www.dianping.com/singapore/hotel'),
                              (u'吉隆坡', 'http://www.dianping.com/kualalumpur/hotel'),
                              (u'墨尔本', 'http://www.dianping.com/melbourne/hotel'),
                              (u'京都', 'http://www.dianping.com/kyoto/hotel'),
                              (u'大阪', 'http://www.dianping.com/osaka/hotel'),
                              (u'北海道', 'http://www.dianping.com/hokkaido/hotel'),
                              (u'清迈', 'http://www.dianping.com/chiangmai/hotel'),
                              (u'芭堤雅', 'http://www.dianping.com/pattaya/hotel'),
                              (u'普吉岛', 'http://www.dianping.com/phuket/hotel'),
                              (u'济州岛', 'http://www.dianping.com/jeju/hotel'),
                              (u'长滩岛', 'http://www.dianping.com/boracay/hotel'),
                              (u'巴厘岛', 'http://www.dianping.com/bali/hotel'),
                              (u'沙巴', 'http://www.dianping.com/sabah/hotel'),
                              (u'纽约', 'http://www.dianping.com/newyork/hotel'),
                              (u'洛杉矶', 'http://www.dianping.com/losangeles/hotel'),
                              (u'巴黎', 'http://www.dianping.com/paris/hotel'),
                              (u'伦敦', 'http://www.dianping.com/london/hotel'),
                              (u'悉尼', 'http://www.dianping.com/sydney/hotel'),
                              (u'奥克兰', 'http://www.dianping.com/auckland/hotel')]

    city_hotel_pingyin = {
        u'丽江': 'http://www.dianping.com/lijiang/hotel',
        u'清迈': 'http://www.dianping.com/chiangmai/hotel',
        u'北海道': 'http://www.dianping.com/hokkaido/hotel',
        u'台州': 'http://www.dianping.com/zhejiangtaizhou/hotel',
        u'巴黎': 'http://www.dianping.com/paris/hotel',
        u'佛山': 'http://www.dianping.com/foshan/hotel',
        u'北京': 'http://www.dianping.com/beijing/hotel',
        u'西安': 'http://www.dianping.com/xian/hotel',
        u'西宁': 'http://www.dianping.com/xining/hotel',
        u'三亚': 'http://www.dianping.com/sanya/hotel',
        u'海口': 'http://www.dianping.com/haikou/hotel',
        u'高雄': 'http://www.dianping.com/kaohsiung/hotel',
        u'绍兴': 'http://www.dianping.com/shaoxing/hotel',
        u'纽约': 'http://www.dianping.com/newyork/hotel',
        u'巴厘岛': 'http://www.dianping.com/bali/hotel',
        u'花莲': 'http://www.dianping.com/hualien/hotel',
        u'长滩岛': 'http://www.dianping.com/boracay/hotel',
        u'新加坡': 'http://www.dianping.com/singapore/hotel',
        u'沙巴': 'http://www.dianping.com/sabah/hotel',
        u'金华': 'http://www.dianping.com/jinhua/hotel',
        u'无锡': 'http://www.dianping.com/wuxi/hotel',
        u'济州岛': 'http://www.dianping.com/jeju/hotel',
        u'乌鲁木齐': 'http://www.dianping.com/wulumuqi/hotel',
        u'普吉岛': 'http://www.dianping.com/phuket/hotel',
        u'廊坊': 'http://www.dianping.com/langfang/hotel',
        u'厦门': 'http://www.dianping.com/xiamen/hotel',
        u'大阪': 'http://www.dianping.com/osaka/hotel',
        u'昆明': 'http://www.dianping.com/kunming/hotel',
        u'深圳': 'http://www.dianping.com/shenzhen/hotel',
        u'宁波': 'http://www.dianping.com/ningbo/hotel',
        u'香港': 'http://www.dianping.com/hongkong/hotel',
        u'苏州': 'http://www.dianping.com/suzhou/hotel',
        u'临沂': 'http://www.dianping.com/linyi/hotel',
        u'银川': 'http://www.dianping.com/yinchuan/hotel',
        u'呼和浩特': 'http://www.dianping.com/huhehaote/hotel',
        u'合肥': 'http://www.dianping.com/hefei/hotel',
        u'台北': 'http://www.dianping.com/taipei/hotel',
        u'南宁': 'http://www.dianping.com/nanning/hotel',
        u'东莞': 'http://www.dianping.com/dongguan/hotel',
        u'成都': 'http://www.dianping.com/chengdu/hotel',
        u'珠海': 'http://www.dianping.com/zhuhai/hotel',
        u'温州': 'http://www.dianping.com/wenzhou/hotel',
        u'上海': 'http://www.dianping.com/shanghai/hotel',
        u'潍坊': 'http://www.dianping.com/weifang/hotel',
        u'武汉': 'http://www.dianping.com/wuhan/hotel',
        u'泰州': 'http://www.dianping.com/taizhou/hotel',
        u'哈尔滨': 'http://www.dianping.com/haerbin/hotel',
        u'淄博': 'http://www.dianping.com/zibo/hotel',
        u'天津': 'http://www.dianping.com/tianjin/hotel',
        u'长沙': 'http://www.dianping.com/changsha/hotel',
        u'烟台': 'http://www.dianping.com/yantai/hotel',
        u'福州': 'http://www.dianping.com/fuzhou/hotel',
        u'吉隆坡': 'http://www.dianping.com/kualalumpur/hotel',
        u'济南': 'http://www.dianping.com/jinan/hotel',
        u'镇江': 'http://www.dianping.com/zhenjiang/hotel',
        u'石家庄': 'http://www.dianping.com/shijiazhuang/hotel',
        u'南昌': 'http://www.dianping.com/nanchang/hotel',
        u'首尔': 'http://www.dianping.com/seoul/hotel',
        u'泰安': 'http://www.dianping.com/taian/hotel',
        u'南通': 'http://www.dianping.com/nantong/hotel',
        u'广州': 'http://www.dianping.com/guangzhou/hotel',
        u'太原': 'http://www.dianping.com/taiyuan/hotel',
        u'悉尼': 'http://www.dianping.com/sydney/hotel',
        u'大连': 'http://www.dianping.com/dalian/hotel',
        u'徐州': 'http://www.dianping.com/xuzhou/hotel',
        u'贵阳': 'http://www.dianping.com/guiyang/hotel',
        u'垦丁': 'http://www.dianping.com/kenting/hotel',
        u'常州': 'http://www.dianping.com/changzhou/hotel',
        u'马鞍山': 'http://www.dianping.com/maanshan/hotel',
        u'惠州': 'http://www.dianping.com/huizhou/hotel',
        u'洛杉矶': 'http://www.dianping.com/losangeles/hotel',
        u'墨尔本': 'http://www.dianping.com/melbourne/hotel',
        u'伦敦': 'http://www.dianping.com/london/hotel',
        u'兰州': 'http://www.dianping.com/lanzhou/hotel',
        u'扬州': 'http://www.dianping.com/yangzhou/hotel',
        u'长春': 'http://www.dianping.com/changchun/hotel',
        u'青岛': 'http://www.dianping.com/qingdao/hotel',
        u'奥克兰': 'http://www.dianping.com/auckland/hotel',
        u'沈阳': 'http://www.dianping.com/shenyang/hotel',
        u'嘉兴': 'http://www.dianping.com/jiaxing/hotel',
        u'芭堤雅': 'http://www.dianping.com/pattaya/hotel',
        u'澳门': 'http://www.dianping.com/macau/hotel',
        u'威海': 'http://www.dianping.com/weihai/hotel',
        u'曼谷': 'http://www.dianping.com/bangkok/hotel',
        u'重庆': 'http://www.dianping.com/chongqing/hotel',
        u'杭州': 'http://www.dianping.com/hangzhou/hotel',
        u'济宁': 'http://www.dianping.com/jining/hotel',
        u'南京': 'http://www.dianping.com/nanjing/hotel',
        u'郑州': 'http://www.dianping.com/zhengzhou/hotel',
        u'东京': 'http://www.dianping.com/tokyo/hotel',
        u'京都': 'http://www.dianping.com/kyoto/hotel'
    }