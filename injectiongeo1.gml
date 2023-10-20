<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/xsl" href="OpenGeoSysGLI.xsl"?>

<OpenGeoSysGLI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogs="http://www.opengeosys.org">
    <name>injectiongeo1</name>
    <points>
        <point id="0" x="0" y="0" z="0" name="origin"/>
        <point id="1" x="18" y="0" z="0"/>
        <point id="2" x="0" y="16" z="0"/>
        <point id="3" x="0" y="0" z="7"/>

        <point id="4" x="18" y="16" z="0"/>
        <point id="5" x="0" y="16" z="7"/>
        <point id="6" x="18" y="0" z="7"/>
        <point id="7" x="18" y="16" z="7"/>
    </points>

    <polylines>
        <polyline id="0" name="front_left">
            <pnt>0</pnt>
            <pnt>3</pnt>
        </polyline>
        <polyline id="1" name="front_right">
            <pnt>2</pnt>
            <pnt>5</pnt>
        </polyline>
        <polyline id="2" name="front_bottom">
            <pnt>3</pnt>
            <pnt>5</pnt>
        </polyline>
        <polyline id="3" name="front_top">
            <pnt>0</pnt>
            <pnt>2</pnt>
        </polyline>
        <polyline id="4" name="bottom_left">
            <pnt>3</pnt>
            <pnt>6</pnt>
        </polyline>
        <polyline id="5" name="bottom_right">
            <pnt>5</pnt>
            <pnt>7</pnt>
        </polyline>
        <polyline id="6" name="top_left">
            <pnt>0</pnt>
            <pnt>1</pnt>
        </polyline>
        <polyline id="7" name="top_right">
            <pnt>2</pnt>
            <pnt>4</pnt>
        </polyline>
        <polyline id="8" name="back_left">
            <pnt>1</pnt>
            <pnt>6</pnt>
        </polyline>
        <polyline id="9" name="back_right">
            <pnt>4</pnt>
            <pnt>7</pnt>
        </polyline>
        <polyline id="10" name="back_bottom">
            <pnt>6</pnt>
            <pnt>7</pnt>
        </polyline>
        <polyline id="11" name="back_top">
            <pnt>1</pnt>
            <pnt>4</pnt>
        </polyline>
    </polylines>
    
    <surfaces>
        <surface id="0" name="front"><!-- x=0 -->
            <element p1="0" p2="3" p3="5"/>
            <element p1="0" p2="2" p3="5"/>
        </surface>
        <surface id="1" name="right"><!-- x=1 -->
            <element p1="2" p2="5" p3="7"/>
            <element p1="2" p2="4" p3="7"/>
        </surface>
        <surface id="2" name="left"><!-- z=1 -->
            <element p1="1" p2="6" p3="3"/>
            <element p1="1" p2="0" p3="3"/>
        </surface>
        <surface id="3" name="back"><!-- z=0 -->
            <element p1="4" p2="7" p3="6"/>
            <element p1="4" p2="1" p3="6"/>
        </surface>
        <surface id="4" name="top"><!-- y=0 -->
            <element p1="1" p2="0" p3="2"/>
            <element p1="1" p2="4" p3="2"/>
        </surface>
        <surface id="5" name="bottom"><!-- y=1 -->
            <element p1="3" p2="6" p3="7"/>
            <element p1="3" p2="5" p3="7"/>
        </surface>
    </surfaces>
</OpenGeoSysGLI>
