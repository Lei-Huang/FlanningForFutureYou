
var jq = $.noConflict();
//ban_qh
jq.fn.banqh = function(can){
	can = jq.extend({
					box:null,//Frame
					pic:null,//Frame of the picture
					prev:null,//right arrow
					next:null,//left arrow
					autoplay:false,//auto display
					interTime:3000,//how long to change to next picture
					delayTime:500,//change time
					order:0,//the number of the currently picture (from 0）
					picdire:true,//direction of the picture change
				}, can || {});
	var picnum = jq(can.pic).find('ul li').length;
	var picw = jq(can.pic).find('ul li').outerWidth(true);
	var pich = jq(can.pic).find('ul li').outerHeight(true);
	var picminnum = jq(can.pnum).find('ul li').length;
	var picminw = jq(can.pnum).find('ul li').outerWidth(true);
	var picminh = jq(can.pnum).find('ul li').outerHeight(true);
	var pictime;
	var tpqhnum=0;
	var xtqhnum=0;
	jq(can.pic).find('ul').width(picnum*picw).height(picnum*pich);
	

	if(can.autoplay==true){
//auto-play
		pictime = setInterval(function(){
			show(tpqhnum);
			minshow(tpqhnum)
			tpqhnum++;
			xtqhnum++;
			if(tpqhnum==picnum){tpqhnum=0};
			if(xtqhnum==picminnum){xtqhnum=0};

		},can.interTime);
		
//if the mouse on the picture, it will stop to auto-play
		jq(can.box).hover(function(){
			clearInterval(pictime);
		},function(){
			pictime = setInterval(function(){
				show(tpqhnum);
				minshow(tpqhnum)
				tpqhnum++;
				xtqhnum++;
				if(tpqhnum==picnum){tpqhnum=0};	
				if(xtqhnum==picminnum){xtqhnum=0};		
				},can.interTime);			
			});
	}

//picture switch
	jq(can.prev).click(function(){
		if(tpqhnum==0){tpqhnum=picnum};
		if(xtqhnum==0){xtqhnum=picnum};
		xtqhnum--;
		tpqhnum--;
		show(tpqhnum);
		minshow(xtqhnum);	
		})
	jq(can.next).click(function(){
		if(tpqhnum==picnum-1){tpqhnum=-1};
		if(xtqhnum==picminnum-1){xtqhnum=-1};
		xtqhnum++;
		minshow(xtqhnum)
		tpqhnum++;
		show(tpqhnum);
		})


	function minshow(xtqhnum){
		var mingdjl_num =xtqhnum-can.min_picnum+2
		var mingdjl_w=-mingdjl_num*picminw;
		var mingdjl_h=-mingdjl_num*picminh;

		if(can.mindire==true){
			jq(can.pnum).find('ul li').css('float','left');
			if(picminnum>can.min_picnum){
				if(xtqhnum<3){mingdjl_w=0;}
				if(xtqhnum==picminnum-1){mingdjl_w=-(mingdjl_num-1)*picminw;}
				jq(can.pnum).find('ul').stop().animate({'left':mingdjl_w},can.delayTime);
				}

		}else{
			jq(can.pnum).find('ul li').css('float','none');
			if(picminnum>can.min_picnum){
				if(xtqhnum<3){mingdjl_h=0;}
				if(xtqhnum==picminnum-1){mingdjl_h=-(mingdjl_num-1)*picminh;}
				jq(can.pnum).find('ul').stop().animate({'top':mingdjl_h},can.delayTime);
				}
			}

	}

//process of image switch
		function show(tpqhnum){
			var gdjl_w=-tpqhnum*picw;
			var gdjl_h=-tpqhnum*pich;
			if(can.picdire==true){
				jq(can.pic).find('ul li').css('float','left');
				jq(can.pic).find('ul').stop().animate({'left':gdjl_w},can.delayTime);
				}else{
			jq(can.pic).find('ul').stop().animate({'top':gdjl_h},can.delayTime);
			}//滚动
			//jq(can.pic).find('ul li').eq(tpqhnum).fadeIn(can.delayTime).siblings('li').fadeOut(can.delayTime);//淡入淡出
			jq(can.pnum).find('li').eq(tpqhnum).addClass("on").siblings(this).removeClass("on");
		};

				
}
