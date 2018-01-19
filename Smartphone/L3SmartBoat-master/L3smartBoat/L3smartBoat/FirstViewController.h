//
//  FirstViewController.h
//  L3smartBoat
//
//  Created by Jerome Godefroy on 22/03/2017.
//  Copyright © 2017 Jerome Godefroy. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <Mapkit/Mapkit.h>

@interface FirstViewController : UIViewController <MKMapViewDelegate, NSURLConnectionDelegate>
{
    NSMutableData *_responseData;
}


@property (weak, nonatomic) IBOutlet MKMapView *mapView;
@property ( nonatomic) NSMutableArray *points;
@end

