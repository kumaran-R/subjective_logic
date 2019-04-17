import React from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Fab from '@material-ui/core/Fab';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import FormLabel from '@material-ui/core/FormLabel';
import Chip from '@material-ui/core/Chip';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing.unit * 2,
        textAlign: 'center',
        color: theme.palette.text.secondary,
    },
});


class CenteredGrid extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            xb1: 0.0,
            xd1: 0.0,
            xu1: 0.0,
            xa1: 0.0,
            xb2: 0.0,
            xd2: 0.0,
            xu2: 0.0,
            xa2: 0.0,
            xfusedopinions: {
                baserate: 0.0,
                belief: 0.0,
                disbelief: 0.0,
                uncertainty: 0.0,
                projectedproba: 0.0

            },

            ynotxb1: 0.0,
            ynotxd1: 0.0,
            ynotxu1: 0.0,
            ynotxa1: 0.0,
            ynotxb2: 0.0,
            ynotxd2: 0.0,
            ynotxu2: 0.0,
            ynotxa2: 0.0,
            ynotxfusedopinions: {
                baserate: 0.0,
                belief: 0.0,
                disbelief: 0.0,
                uncertainty: 0.0,
                projectedproba: 0.0
            },


            yxb1: 0.0,
            yxd1: 0.0,
            yxu1: 0.0,
            yxa1: 0.0,
            yxb2: 0.0,
            yxd2: 0.0,
            yxu2: 0.0,
            yxa2: 0.0,
            yxfusedopinions: {
                baserate: 0.0,
                belief: 0.0,
                disbelief: 0.0,
                uncertainty: 0.0,
                projectedproba: 0.0
            },


        }
    }

    handleChange = name => event => {
        this.setState({[name]: event.target.value});
    };


    calculateXFusion() {
        let a1 = {
            baserate: Number(this.state.xa1),
            uncertainty: Number(this.state.xu1),
            belief: Number(this.state.xb1),
            disbelief: Number(this.state.xd1),
            projectedproba: Number(this.state.xb1) + Number(this.state.xa1) * Number(this.state.xu1)
        };


        let a2 = {
            baserate: Number(this.state.xa2),
            uncertainty: Number(this.state.xu2),
            belief: Number(this.state.xb2),
            disbelief: Number(this.state.xd2),
            projectedproba: Number(this.state.xb2) + Number(this.state.xa2) * Number(this.state.xu2)
        };


        console.log({a1: a1, a2: a2})

        let fusedXopinions

        if (this.state.xFusionOperator === "cumulative") {
            fusedXopinions = this.CumulativeFusion(a1, a2);
        } else {
            fusedXopinions = this.AveragingFusion(a1, a2);
        }


        this.setState({
            xfusedopinions: fusedXopinions,
        })

        console.log(fusedXopinions)

    }

    calculateYXFusion() {
        let a1 = {
            baserate: Number(this.state.yxa1),
            uncertainty: Number(this.state.yxu1),
            belief: Number(this.state.yxb1),
            disbelief: Number(this.state.yxd1),
            projectedproba: Number(this.state.yxb1) + Number(this.state.yxa1) * Number(this.state.yxu1)
        };


        let a2 = {
            baserate: Number(this.state.yxa2),
            uncertainty: Number(this.state.yxu2),
            belief: Number(this.state.yxb2),
            disbelief: Number(this.state.yxd2),
            projectedproba: Number(this.state.yxb2) + Number(this.state.yxa2) * Number(this.state.yxu2)
        };


        console.log({a1: a1, a2: a2})

        let fusedXopinions

        if (this.state.yxFusionOperator === "cumulative") {
            fusedXopinions = this.CumulativeFusion(a1, a2);
        } else {
            fusedXopinions = this.AveragingFusion(a1, a2);
        }


        this.setState({
            yxfusedopinions: fusedXopinions,
        })

        console.log(fusedXopinions)

    }

    calculateYNotXFusion() {
        let a1 = {
            baserate: Number(this.state.ynotxa1),
            uncertainty: Number(this.state.ynotxu1),
            belief: Number(this.state.ynotxb1),
            disbelief: Number(this.state.ynotxd1),
            projectedproba: Number(this.state.ynotxb1) + Number(this.state.ynotxa1) * Number(this.state.ynotxu1)
        };


        let a2 = {
            baserate: Number(this.state.ynotxa2),
            uncertainty: Number(this.state.ynotxu2),
            belief: Number(this.state.ynotxb2),
            disbelief: Number(this.state.ynotxd2),
            projectedproba: Number(this.state.ynotxb2) + Number(this.state.ynotxa2) * Number(this.state.ynotxu2)
        };


        console.log({a1: a1, a2: a2})

        let fusedXopinions

        if (this.state.ynotxFusionOperator === "cumulative") {
            fusedXopinions = this.CumulativeFusion(a1, a2);
        } else {
            fusedXopinions = this.AveragingFusion(a1, a2);
        }


        this.setState({
            ynotxfusedopinions: fusedXopinions,
        })

        console.log(fusedXopinions)

    }


    calculateDeduction() {

        let x = this.state.xfusedopinions

        let yx = this.state.yxfusedopinions

        let ynotx = this.state.ynotxfusedopinions


        let deducedOpinions

        if (x && yx && ynotx) {

            let arg1 = [yx, ynotx]
            let arg2 = x

            deducedOpinions = this.Deduction(arg1, arg2)
        }

        this.setState({
            deducedOpinions: deducedOpinions
        })

    }


    /**
     * CumulativeFusion
     **/

    CumulativeFusion(arg_1, arg_2) {

        let a1 = arg_1.baserate, a2 = arg_2.baserate,
            b1 = arg_1.belief, b2 = arg_2.belief,
            u1 = arg_1.uncertainty, u2 = arg_2.uncertainty;
        let u, b, a;
        if (u1 !== 0 || u2 !== 0) {
            b = (b1 * u2 + b2 * u1) / (u1 + u2 - u1 * u2);
            u = u1 * u2 / (u1 + u2 - u1 * u2);
            a = (u1 !== 1 || u2 !== 1) ? (a1 * u2 + a2 * u1 - (a1 + a2) * u1 * u2) / (u1 + u2 - 2 * u1 * u2) : (a1 + a2) / 2;
        } else {
            b = 0.5 * (b1 + b2);
            u = 0;
            a = 0.5 * (a1 + a2);
        }

        return {
            baserate: a,
            uncertainty: u,
            belief: b,
            disbelief: 1 - u - b,
            projectedproba: b + a * u
        };
    };

    /**
     * AveragingFusion
     **/

    AveragingFusion(arg_1, arg_2) {
        let a1 = arg_1.baserate, a2 = arg_2.baserate,
            b1 = arg_1.belief, b2 = arg_2.belief,
            u1 = arg_1.uncertainty, u2 = arg_2.uncertainty,
            e1 = arg_1.projectedproba, e2 = arg_2.projectedproba;

        let u, b, a;
        if (u1 !== 0 || u2 !== 0) {
            b = (b1 * u2 + b2 * u1) / (u1 + u2);
            u = 2 * u1 * u2 / (u1 + u2);
            a = (a1 + a2) / 2;
        } else {
            b = 0.5 * (b1 + b2);
            u = 0;
            a = 0.5 * (a1 + a2);
        }

        return {
            baserate: a,
            uncertainty: u,
            belief: b,
            disbelief: 1 - u - b,
            projectedproba: b + a * u
        };
    };


    /**
     * Deduction
     **/

    Deduction(arg_1, arg_2) {


        if (arg_1.length < 2) return null;

        let ax = arg_2.baserate,
            bx = arg_2.belief,
            dx = arg_2.disbelief,
            ux = arg_2.uncertainty,
            ex = arg_2.projectedproba;
        let ay = arg_1[0].baserate,
            b0 = arg_1[0].belief,
            d0 = arg_1[0].disbelief,
            u0 = arg_1[0].uncertainty,
            e0 = arg_1[0].projectedproba;
        let b1 = arg_1[1].belief,
            d1 = arg_1[1].disbelief,
            u1 = arg_1[1].uncertainty,
            e1 = arg_1[1].projectedproba;


        let bIy = bx * b0 + dx * b1 + ux * (b0 * ax + b1 * (1 - ax)),
            dIy = bx * d0 + dx * d1 + ux * (d0 * ax + d1 * (1 - ax)),
            uIy = bx * u0 + dx * u1 + ux * (u0 * ax + u1 * (1 - ax));
        let Pyvacuousx = b0 * ax + b1 * (1 - ax) + ay * (u0 * ax + u1 * (1 - ax));

        let K;


        if (((b0 > b1) && (d0 > d1)) || ((b0 <= b1) && (d0 <= d1))) { //CASE I

            K = 0;
        } else if ((b0 > b1) && (d0 <= d1)) { //CASE II

            if (Pyvacuousx <= (b1 + ay * (1 - b1 - d0))) { //CASE A

                if (ex <= ax) { //Case 1
                    K = ax * ux * (bIy - b1) / (ay * ex);
                } else { //Case 2
                    K = ax * ux * (dIy - d0) * (b0 - b1) / ((dx + (1 - ax) * ux) * ay * (d1 - d0));
                }
            } else { //CASE B

                if (ex <= ax) { //Case 1
                    K = (1 - ax) * ux * (bIy - b1) * (d1 - d0) / (ex * (1 - ay) * (b0 - b1));
                } else { //Case 2
                    K = (1 - ax) * ux * (dIy - d0) / ((1 - ay) * (dx + (1 - ax) * ux));
                }
            }
        } else { //CASE III

            if (Pyvacuousx <= (b1 + ay * (1 - b1 - d0))) { //CASE A
                if (ex <= ax) { //Case 1
                    K = (1 - ax) * ux * (dIy - d1) * (b1 - b0) / (ex * ay * (d0 - d1));
                } else { //Case 2
                    K = (1 - ax) * ux * (bIy - b0) / (ay * (dx + (1 - ax) * ux));
                }
            } else { //CASE B
                if (ex <= ax) { //Case 1
                    K = ax * ux * (dIy - d1) / (ex * (1 - ay));
                } else { //Case 2
                    K = ax * ux * (bIy - b0) * (d0 - d1) / ((1 - ay) * (b1 - b0) * (dx + (1 - ax) * ux));
                }
            }
        }

        if (isNaN(K) || !isFinite(K)) K = 0;

        let by = bIy - ay * K,
            dy = dIy - (1 - ay) * K,
            uy = uIy + K;
        let ey = by + ay * uy;

        return {
            baserate: ay,
            uncertainty: uy,
            belief: by,
            disbelief: dy,
            projectedproba: ey
        };
    };


    render() {
        const {classes} = this.props;
        return (
            <div className={classes.root}>
                <Grid container spacing={24} style={{width: "100%", margin: 0}}>

                    <AppBar position="static">
                        <Toolbar>

                            <Typography variant="h6" color="inherit" className={classes.grow}>
                                Subjective Logic
                            </Typography>
                        </Toolbar>
                    </AppBar>

                    <Grid item xs={12}>
                        <Paper className={classes.paper} style={{background: "#ff9800"}}>
                            <Grid container spacing={24}>

                                <Grid item xs={12}>
                                    <b> Opinions of X </b>
                                </Grid>


                                <Grid item xs={10}>
                                    <Grid container spacing={24}>
                                        <Grid item xs={6}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24}>
                                                    <Grid item xs={12}>
                                                        Agent 1 opinions
                                                    </Grid>

                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="belief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xb1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="disbelief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xd1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="uncertainty"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xu1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="base rate"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xa1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>
                                        <Grid item xs={6}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24}>
                                                    <Grid item xs={12}>
                                                        Agent 2 opinions
                                                    </Grid>

                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="belief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xb2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="disbelief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xd2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="uncertainty"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xu2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="base rate"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('xa2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,

                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>


                                        <Grid item xs={12}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24} style={{height: "70px"}}>
                                                    <Grid xs={12}>
                                                        Fused Opinions
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Belief = " + this.state.xfusedopinions.belief}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Disbelief = " + this.state.xfusedopinions.disbelief}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                    <Grid xs={3}>
                                                        <Chip
                                                            label={"Uncertainty = " + this.state.xfusedopinions.uncertainty}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Baserate = " + this.state.xfusedopinions.baserate}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Projected Probability = " + this.state.xfusedopinions.projectedproba}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>
                                    </Grid>

                                </Grid>


                                <Grid item xs={2}>
                                    <Paper className={classes.paper}>
                                        <Grid container spacing={24}>
                                            <Grid item xs={12}>
                                                Fusion Operator
                                            </Grid>

                                            <Grid item xs={12}>
                                                <FormControl component="fieldset" className={classes.formControl}>
                                                    <RadioGroup
                                                        aria-label="Gender"
                                                        name="gender1"
                                                        className={classes.group}
                                                        value={this.state.value}
                                                        onChange={this.handleChange("xFusionOperator")}
                                                    >
                                                        <FormControlLabel value="cumulative" control={<Radio/>}
                                                                          label="Cumulative Fusion"/>
                                                        <FormControlLabel value="average" control={<Radio/>}
                                                                          label="Average Fusion"/>

                                                    </RadioGroup>
                                                </FormControl>
                                            </Grid>


                                            <Grid item xs={12}>
                                                <Fab color="primary" aria-label="Add" className={classes.fab}
                                                     onClick={this.calculateXFusion.bind(this)}>
                                                    Fuse
                                                </Fab>
                                            </Grid>
                                        </Grid>


                                    </Paper>
                                </Grid>
                            </Grid>

                        </Paper>
                    </Grid>

                    <Grid item xs={12}>
                        <Paper className={classes.paper} style={{background: "#4caf50"}}>
                            <Grid container spacing={24}>

                                <Grid item xs={12}>
                                    <b> Opinions of Y|X </b>
                                </Grid>


                                <Grid item xs={10}>
                                    <Grid container spacing={24}>
                                        <Grid item xs={6}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24}>
                                                    <Grid item xs={12}>
                                                        Agent 1 opinions
                                                    </Grid>

                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="belief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxb1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="disbelief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxd1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="uncertainty"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxu1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="base rate"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxa1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>
                                        <Grid item xs={6}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24}>
                                                    <Grid item xs={12}>
                                                        Agent 2 opinions
                                                    </Grid>

                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="belief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxb2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="disbelief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxd2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="uncertainty"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxu2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="base rate"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('yxa2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>


                                        <Grid item xs={12}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24} style={{height: "70px"}}>
                                                    <Grid xs={12}>
                                                        Fused Opinions
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Belief = " + this.state.yxfusedopinions.belief}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Disbelief = " + this.state.yxfusedopinions.disbelief}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                    <Grid xs={3}>
                                                        <Chip
                                                            label={"Uncertainty = " + this.state.yxfusedopinions.uncertainty}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Baserate = " + this.state.yxfusedopinions.baserate}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Projected Probability = " + this.state.yxfusedopinions.projectedproba}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>
                                    </Grid>

                                </Grid>


                                <Grid item xs={2}>
                                    <Paper className={classes.paper}>
                                        <Grid container spacing={24}>
                                            <Grid item xs={12}>
                                                Fusion Operator
                                            </Grid>

                                            <Grid item xs={12}>
                                                <FormControl component="fieldset" className={classes.formControl}>
                                                    <RadioGroup
                                                        aria-label="Gender"
                                                        name="gender1"
                                                        className={classes.group}
                                                        value={this.state.value}
                                                        onChange={this.handleChange("yxFusionOperator")}
                                                    >
                                                        <FormControlLabel value="cumulative" control={<Radio/>}
                                                                          label="Cumulative Fusion"/>
                                                        <FormControlLabel value="average" control={<Radio/>}
                                                                          label="Average Fusion"/>

                                                    </RadioGroup>
                                                </FormControl>
                                            </Grid>


                                            <Grid item xs={12}>
                                                <Fab color="primary" aria-label="Add" className={classes.fab}
                                                     onClick={this.calculateYXFusion.bind(this)}>
                                                    Fuse
                                                </Fab>
                                            </Grid>
                                        </Grid>


                                    </Paper>
                                </Grid>
                            </Grid>

                        </Paper>
                    </Grid>

                    <Grid item xs={12}>
                        <Paper className={classes.paper} style={{background: "#8bc34a"}}>
                            <Grid container spacing={24}>

                                <Grid item xs={12}>
                                    <b> Opinions of Y|~X </b>
                                </Grid>


                                <Grid item xs={10}>
                                    <Grid container spacing={24}>
                                        <Grid item xs={6}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24}>
                                                    <Grid item xs={12}>
                                                        Agent 1 opinions
                                                    </Grid>

                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="belief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxb1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="disbelief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxd1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="uncertainty"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxu1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="base rate"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxa1')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>
                                        <Grid item xs={6}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24}>
                                                    <Grid item xs={12}>
                                                        Agent 2 opinions
                                                    </Grid>

                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="belief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxb2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="disbelief"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxd2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="uncertainty"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxu2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <TextField
                                                            id="standard-number"
                                                            label="base rate"
                                                            value={this.state.age}
                                                            onChange={this.handleChange('ynotxa2')}
                                                            type="number"
                                                            className={classes.textField}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                            margin="normal"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>


                                        <Grid item xs={12}>
                                            <Paper className={classes.paper}>
                                                <Grid container spacing={24} style={{height: "70px"}}>
                                                    <Grid xs={12}>
                                                        Fused Opinions
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Belief = " + this.state.ynotxfusedopinions.belief}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Disbelief = " + this.state.ynotxfusedopinions.disbelief}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                    <Grid xs={3}>
                                                        <Chip
                                                            label={"Uncertainty = " + this.state.ynotxfusedopinions.uncertainty}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Baserate = " + this.state.ynotxfusedopinions.baserate}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>

                                                    <Grid xs={2}>
                                                        <Chip
                                                            label={"Projected Probability = " + this.state.ynotxfusedopinions.projectedproba}
                                                            className={classes.chip}
                                                            color="primary"
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Paper>
                                        </Grid>
                                    </Grid>

                                </Grid>


                                <Grid item xs={2}>
                                    <Paper className={classes.paper}>
                                        <Grid container spacing={24}>
                                            <Grid item xs={12}>
                                                Fusion Operator
                                            </Grid>

                                            <Grid item xs={12}>
                                                <FormControl component="fieldset" className={classes.formControl}>
                                                    <RadioGroup
                                                        aria-label="Gender"
                                                        name="gender1"
                                                        className={classes.group}
                                                        value={this.state.value}
                                                        onChange={this.handleChange("ynotxFusionOperator")}
                                                    >
                                                        <FormControlLabel value="cumulative" control={<Radio/>}
                                                                          label="Cumulative Fusion"/>
                                                        <FormControlLabel value="average" control={<Radio/>}
                                                                          label="Average Fusion"/>

                                                    </RadioGroup>
                                                </FormControl>
                                            </Grid>


                                            <Grid item xs={12}>
                                                <Fab color="primary" aria-label="Add" className={classes.fab}
                                                     onClick={this.calculateYNotXFusion.bind(this)}>
                                                    Fuse
                                                </Fab>
                                            </Grid>
                                        </Grid>


                                    </Paper>
                                </Grid>
                            </Grid>

                        </Paper>
                    </Grid>


                    <Grid item xs={12}></Grid>
                    {
                        (this.state.xfusedopinions && this.state.yxfusedopinions && this.state.ynotxfusedopinions) &&
                        <Grid item xs={12}>
                            <Paper className={classes.paper} style={{background: "#93c3c0"}}>
                                <Grid container spacing={24}>

                                    <Grid item xs={12}>
                                        <b> Deduce Opinions </b>
                                    </Grid>

                                    <Grid item xs={12}>
                                        <Grid container spacing={24}>
                                            <Grid item xs={3}>
                                                <Paper className={classes.paper}>
                                                    <Grid item xs={12}>

                                                        <b> Y|X </b>
                                                    </Grid>
                                                    <Grid item xs={12}>

                                                        <Grid container spacing={24} style={{textAlign: "left"}}>

                                                            <Grid item xs={12}>
                                                                {"Belief = " + this.state.yxfusedopinions.belief}

                                                            </Grid>
                                                            <Grid item xs={12}>
                                                                {"Disbelief = " + this.state.yxfusedopinions.disbelief}

                                                            </Grid>
                                                            <Grid item xs={12}>
                                                                {"Uncertainty = " + this.state.yxfusedopinions.uncertainty}

                                                            </Grid>

                                                            <Grid item xs={12}>
                                                                {"Baserate = " + this.state.yxfusedopinions.baserate}

                                                            </Grid>

                                                            <Grid item xs={12}>
                                                                {"Projected Probability = " + this.state.yxfusedopinions.projectedproba}

                                                            </Grid>
                                                        </Grid>
                                                    </Grid>

                                                </Paper>
                                            </Grid>
                                            <Grid item xs={3}>

                                                <Paper className={classes.paper}>
                                                    <Grid item xs={12}>
                                                        <b> Y|~X </b>
                                                    </Grid>

                                                    <Grid container spacing={24} style={{textAlign: "left"}}>

                                                        <Grid item xs={12}>
                                                            {"Belief = " + this.state.ynotxfusedopinions.belief}

                                                        </Grid>
                                                        <Grid item xs={12}>
                                                            {"Disbelief = " + this.state.ynotxfusedopinions.disbelief}

                                                        </Grid>
                                                        <Grid item xs={12}>
                                                            {"Uncertainty = " + this.state.ynotxfusedopinions.uncertainty}

                                                        </Grid>

                                                        <Grid item xs={12}>
                                                            {"Baserate = " + this.state.ynotxfusedopinions.baserate}

                                                        </Grid>

                                                        <Grid item xs={12}>
                                                            {"Projected Probability = " + this.state.ynotxfusedopinions.projectedproba}

                                                        </Grid>
                                                    </Grid>
                                                </Paper>

                                            </Grid>

                                            <Grid item xs={1}>
                                                Deduce
                                            </Grid>

                                            <Grid item xs={3}>
                                                <Paper className={classes.paper}>
                                                    <Grid item xs={12}>
                                                        <b> X </b>
                                                    </Grid>
                                                    <Grid container spacing={24}
                                                          style={{textAlign: "left"}}>

                                                        <Grid item xs={12}>
                                                            {"Belief = " + this.state.xfusedopinions.belief}

                                                        </Grid>
                                                        <Grid item xs={12}>
                                                            {"Disbelief = " + this.state.xfusedopinions.disbelief}

                                                        </Grid>
                                                        <Grid item xs={12}>
                                                            {"Uncertainty = " + this.state.xfusedopinions.uncertainty}

                                                        </Grid>

                                                        <Grid item xs={12}>
                                                            {"Baserate = " + this.state.xfusedopinions.baserate}

                                                        </Grid>

                                                        <Grid item xs={12}>
                                                            {"Projected Probability = " + this.state.xfusedopinions.projectedproba}

                                                        </Grid>

                                                    </Grid>
                                                </Paper>
                                            </Grid>


                                            <Grid item xs={2} alignItems={"center"}>
                                                <Grid container>
                                                    <Grid item xs={12}>
                                                        <Paper className={classes.paper}>
                                                            <Fab color="primary" aria-label="Add"
                                                                 className={classes.fab}
                                                                 onClick={this.calculateDeduction.bind(this)}>
                                                                Deduce
                                                            </Fab>
                                                        </Paper>
                                                    </Grid>
                                                </Grid>
                                                {
                                                    this.state.deducedOpinions &&
                                                    <Grid container style={{marginTop:"10px",textAlign:"left"}}>
                                                        <Grid item xs={12}>
                                                            <Paper className={classes.paper} style={{textAlign:"left"}}>
                                                                <Grid item xs={12}>Belief = {this.state.deducedOpinions.belief}</Grid>
                                                                <Grid item xs={12}>Disbelief = {this.state.deducedOpinions.disbelief}</Grid>
                                                                <Grid item xs={12}>Uncertainty = {this.state.deducedOpinions.uncertainty}</Grid>
                                                                <Grid item xs={12}>Baserate = {this.state.deducedOpinions.baserate}</Grid>
                                                                <Grid item xs={12}>Projected Probability = {this.state.deducedOpinions.projectedproba}</Grid>
                                                            </Paper>
                                                        </Grid>
                                                    </Grid>
                                                }

                                            </Grid>
                                        </Grid>
                                    </Grid>
                                </Grid>
                            </Paper>
                        </Grid>
                    }

                </Grid>
            </div>
        );

    }

}

CenteredGrid.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(CenteredGrid);