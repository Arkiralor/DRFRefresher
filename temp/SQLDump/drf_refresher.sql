--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

-- Started on 2022-06-07 02:42:14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 44480)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO prithoo;

--
-- TOC entry 215 (class 1259 OID 44479)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO prithoo;

--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 215
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 218 (class 1259 OID 44489)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO prithoo;

--
-- TOC entry 217 (class 1259 OID 44488)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO prithoo;

--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 217
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 214 (class 1259 OID 44473)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO prithoo;

--
-- TOC entry 213 (class 1259 OID 44472)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO prithoo;

--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 213
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 226 (class 1259 OID 44600)
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id uuid NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO prithoo;

--
-- TOC entry 225 (class 1259 OID 44579)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id uuid NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO prithoo;

--
-- TOC entry 224 (class 1259 OID 44578)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO prithoo;

--
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 224
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 212 (class 1259 OID 44464)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO prithoo;

--
-- TOC entry 211 (class 1259 OID 44463)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO prithoo;

--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 211
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 210 (class 1259 OID 44455)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO prithoo;

--
-- TOC entry 209 (class 1259 OID 44454)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO prithoo;

--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 209
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 227 (class 1259 OID 44613)
-- Name: django_session; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO prithoo;

--
-- TOC entry 228 (class 1259 OID 44622)
-- Name: storyapp_story; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.storyapp_story (
    id uuid NOT NULL,
    title character varying(250) NOT NULL,
    slug character varying(250),
    description text,
    body text NOT NULL,
    genre character varying(32),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    author_id uuid NOT NULL
);


ALTER TABLE public.storyapp_story OWNER TO prithoo;

--
-- TOC entry 219 (class 1259 OID 44521)
-- Name: userapp_user; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.userapp_user (
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    id uuid NOT NULL,
    email character varying(254) NOT NULL,
    user_phone_primary character varying(10),
    user_slug character varying(250),
    user_type character varying(32)
);


ALTER TABLE public.userapp_user OWNER TO prithoo;

--
-- TOC entry 221 (class 1259 OID 44533)
-- Name: userapp_user_groups; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.userapp_user_groups (
    id bigint NOT NULL,
    user_id uuid NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.userapp_user_groups OWNER TO prithoo;

--
-- TOC entry 220 (class 1259 OID 44532)
-- Name: userapp_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.userapp_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userapp_user_groups_id_seq OWNER TO prithoo;

--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 220
-- Name: userapp_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.userapp_user_groups_id_seq OWNED BY public.userapp_user_groups.id;


--
-- TOC entry 223 (class 1259 OID 44540)
-- Name: userapp_user_user_permissions; Type: TABLE; Schema: public; Owner: prithoo
--

CREATE TABLE public.userapp_user_user_permissions (
    id bigint NOT NULL,
    user_id uuid NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.userapp_user_user_permissions OWNER TO prithoo;

--
-- TOC entry 222 (class 1259 OID 44539)
-- Name: userapp_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: prithoo
--

CREATE SEQUENCE public.userapp_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userapp_user_user_permissions_id_seq OWNER TO prithoo;

--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 222
-- Name: userapp_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prithoo
--

ALTER SEQUENCE public.userapp_user_user_permissions_id_seq OWNED BY public.userapp_user_user_permissions.id;


--
-- TOC entry 3218 (class 2604 OID 44483)
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 3219 (class 2604 OID 44492)
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 3217 (class 2604 OID 44476)
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 3222 (class 2604 OID 44582)
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 3216 (class 2604 OID 44467)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 3215 (class 2604 OID 44458)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 3220 (class 2604 OID 44536)
-- Name: userapp_user_groups id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_groups ALTER COLUMN id SET DEFAULT nextval('public.userapp_user_groups_id_seq'::regclass);


--
-- TOC entry 3221 (class 2604 OID 44543)
-- Name: userapp_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.userapp_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 3445 (class 0 OID 44480)
-- Dependencies: 216
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 3447 (class 0 OID 44489)
-- Dependencies: 218
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 3443 (class 0 OID 44473)
-- Dependencies: 214
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add Token	6	add_token
22	Can change Token	6	change_token
23	Can delete Token	6	delete_token
24	Can view Token	6	view_token
25	Can add token	7	add_tokenproxy
26	Can change token	7	change_tokenproxy
27	Can delete token	7	delete_tokenproxy
28	Can view token	7	view_tokenproxy
29	Can add User	8	add_user
30	Can change User	8	change_user
31	Can delete User	8	delete_user
32	Can view User	8	view_user
33	Can add Story	9	add_story
34	Can change Story	9	change_story
35	Can delete Story	9	delete_story
36	Can view Story	9	view_story
\.


--
-- TOC entry 3455 (class 0 OID 44600)
-- Dependencies: 226
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
\.


--
-- TOC entry 3454 (class 0 OID 44579)
-- Dependencies: 225
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-06-06 23:01:04.814614+05:30	06f621c6-8a9a-41ea-8f14-0a0640f35cda	admin	2	[{"changed": {"fields": ["First name", "Last name", "User phone primary", "User type"]}}]	8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
2	2022-06-06 23:03:05.545723+05:30	bfeea150-10ae-4fcd-8e2a-9522389fa4f1	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
3	2022-06-06 23:05:42.671721+05:30	40f5ea5e-38da-4bff-bfcc-fef1ef4b2267	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
4	2022-06-06 23:08:59.453361+05:30	a5bb9271-479b-43b5-9145-f57845fe7b94	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
5	2022-06-06 23:11:13.86767+05:30	41c253e2-3768-4d79-80c0-4a3957092c89	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
6	2022-06-06 23:14:03.684883+05:30	72dd711c-12ee-4ab0-b802-629ce60f769f	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
7	2022-06-06 23:18:11.437812+05:30	8c9638f2-9c68-43fa-a4ed-d8eafad20c63	After College by testuser_001	1	[{"added": {}}]	9	06f621c6-8a9a-41ea-8f14-0a0640f35cda
8	2022-06-06 23:20:04.188364+05:30	8c9638f2-9c68-43fa-a4ed-d8eafad20c63	After College by testuser_001	3		9	06f621c6-8a9a-41ea-8f14-0a0640f35cda
9	2022-06-06 23:29:59.479374+05:30	13275e60-05f2-4dba-922f-2bdc3686a140	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
10	2022-06-06 23:31:18.364007+05:30	e9ba10fa-2272-4ead-ada1-8b63cc3d5c9a	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
11	2022-06-06 23:35:26.272334+05:30	495b7107-e5dc-4028-9a83-32d37a11bbc2	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
12	2022-06-06 23:37:45.644269+05:30	71122657-e988-4895-8769-fa9634b62bbe	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
13	2022-06-06 23:48:50.297913+05:30	e8f2fd70-9126-4f06-aa26-12efe9b5ca40	testuser_001	3		8	06f621c6-8a9a-41ea-8f14-0a0640f35cda
14	2022-06-06 23:52:11.001129+05:30	c6858829-1317-495e-ae5d-e9aad0aefc83	After College by testuser_001	1	[{"added": {}}]	9	06f621c6-8a9a-41ea-8f14-0a0640f35cda
\.


--
-- TOC entry 3441 (class 0 OID 44464)
-- Dependencies: 212
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	authtoken	token
7	authtoken	tokenproxy
8	userapp	user
9	storyapp	story
\.


--
-- TOC entry 3439 (class 0 OID 44455)
-- Dependencies: 210
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-06-06 22:56:13.205907+05:30
2	contenttypes	0002_remove_content_type_name	2022-06-06 22:56:13.237167+05:30
3	auth	0001_initial	2022-06-06 22:56:13.284004+05:30
4	auth	0002_alter_permission_name_max_length	2022-06-06 22:56:13.29966+05:30
5	auth	0003_alter_user_email_max_length	2022-06-06 22:56:13.29966+05:30
6	auth	0004_alter_user_username_opts	2022-06-06 22:56:13.315251+05:30
7	auth	0005_alter_user_last_login_null	2022-06-06 22:56:13.315251+05:30
8	auth	0006_require_contenttypes_0002	2022-06-06 22:56:13.315251+05:30
9	auth	0007_alter_validators_add_error_messages	2022-06-06 22:56:13.330875+05:30
10	auth	0008_alter_user_username_max_length	2022-06-06 22:56:13.330875+05:30
11	auth	0009_alter_user_last_name_max_length	2022-06-06 22:56:13.346542+05:30
12	auth	0010_alter_group_name_max_length	2022-06-06 22:56:13.346542+05:30
13	auth	0011_update_proxy_permissions	2022-06-06 22:56:13.362123+05:30
14	auth	0012_alter_user_first_name_max_length	2022-06-06 22:56:13.362123+05:30
15	userapp	0001_initial	2022-06-06 22:56:13.440248+05:30
16	admin	0001_initial	2022-06-06 22:56:13.471498+05:30
17	admin	0002_logentry_remove_auto_add	2022-06-06 22:56:13.48713+05:30
18	admin	0003_logentry_add_action_flag_choices	2022-06-06 22:56:13.48713+05:30
19	authtoken	0001_initial	2022-06-06 22:56:13.502791+05:30
20	authtoken	0002_auto_20160226_1747	2022-06-06 22:56:13.534006+05:30
21	authtoken	0003_tokenproxy	2022-06-06 22:56:13.534006+05:30
22	sessions	0001_initial	2022-06-06 22:56:13.549629+05:30
23	storyapp	0001_initial	2022-06-06 22:56:13.580878+05:30
24	storyapp	0002_initial	2022-06-06 22:56:13.596498+05:30
\.


--
-- TOC entry 3456 (class 0 OID 44613)
-- Dependencies: 227
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
a6s8z0u42bcjdvkzed66p49vmvb0had7	.eJxVjEsOwiAQQO_CWshAYRCX7j1DMzCDrZo26WdlvLtt0oWu3-etWlqXrl1nmdqe1UUBVnS2oD5TIu2tkD5X6zUQoIfahMKkTr9ZpvKUYW_5QcN9NGUclqnPZlfMQWdzG1le18P9G3Q0d1udskPILiUo2DCJs4kdkUSUFAJYCy5AzDFWcSkiB89cGnK58oZqVp8v0XxA9Q:1nyGYe:PYEKcBM1CjlMbt9sA1QfxtjoJ1qciqKbJFltbN4opR8	2022-06-20 23:00:28.556898+05:30
\.


--
-- TOC entry 3457 (class 0 OID 44622)
-- Dependencies: 228
-- Data for Name: storyapp_story; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.storyapp_story (id, title, slug, description, body, genre, created_at, updated_at, author_id) FROM stdin;
c6858829-1317-495e-ae5d-e9aad0aefc83	After College	after-college-testuser_001	A short personal summary of life after college but before beginning your career.	So, as you all know I recently completed my post-graduation and am now sitting at home. I am not actively looking for a job right now as there are things I need to learn before I can even apply for a job, since college trains you on the workings of the subject, how everything works and why. It absolutely doesn’t prepare you for the job market; it can’t do that even if it wanted to since job requirements and specifications change every other year and nowhere else is this more apparent than in computer science. College is supposed to teach you the ins and outs of the subject, not what you need to do in an occupation, you will be able to figure that out on your own in your own time if you know how everything works. If you want to learn how to do a job then it is vocational training you are looking for, not a college degree. College is a place of higher learning, not a place for job-training; which is why I find it so very absurd that job providers expect new recruits to know everything about a job with minimal training even though they want a college degree on your résumé and not a certificate from a vocational institute.\r\n\r\nBut no, I am not here to talk about how the job-market in my country is flawed in its recruitment strategies and how all the moguls seem to disregard any and all changes suggested by experts. That’s a landmine with educated morons giving out falsified anecdotal accounts of why proven paradigms and actual research suggesting a serious flaw in the system are wrong and they are right, since they know all that is to know even though they probably never worked at more than two positions from maybe three highly urbanized cities, in their life. Yes, yes, I know that that was a glaring generalization but sometimes these functional idiots get on my nerves.\r\n\r\nWhat I am here to talk about, instead is the sudden sense of emptiness and loneliness that starts to consume you the day your college life ends and you find yourself staring out through the window from a chair or up at the ceiling from your bed with absolutely nothing to do all day. All the friends you made over the course of these last few years have suddenly moved away, back to their hometowns or to other cities to find jobs or to start their lives (yes, I know they probably feel the same but I am writing this from my own perspective) and you do not even have people left that you can hang out with or go places with because for the last several years, they were the vast majority of your social circle. There are so many articles and books by so-called ‘life-coaches’ that tell you what to do after college but aside from the fact that most of them are utter-bullshit and probably written by someone with absolutely no connection to the real world, the fact remains that all of these are long-term plans; nothing ever tells you effectively what to do in your day-to-day. Some tell you to learn a singular new skill which is good, but then they say that you should only do that in your free time, everything else can wait, do nothing else, no need to relax and no need for leisurely activities. Like thanks, crazy person who probably needs some serious therapy and probably only wrote this article for the $15 the publisher promised, I will do exactly that. It is not like I just spent up to four years doing the exact same thing that probably messed up my psychological characteristics to such a degree that I will probably be paying for that for the rest of my life. Nope, I will continue doing that and just mess up myself even more, by acting like a machine and neglecting my mental health and social relationships and any and all soft-skills that I have somehow managed to retain these past few years despite the life I have led.\r\n\r\nBut they do manage to get one thing right: learning a new skill is a great way to ward away those feelings of emptiness and loneliness that always accompany the period between the end of your college life and the start of your career, just maybe not learn it with the intensity they suggest? I seriously think we have enough people skilled in a field with absolutely no social skills or emotional intelligence. Barring that, do anything to fill up your empty time: volunteer, go to new events, try arts and crafts and of course, meet new people, see what the city/town/village you live in is like now; but still leave yourself with some free time. You just spent years roughly sticking to a strict schedule and will probably spend the rest of your life doing the same once you start your career. So just for this once, give yourself at least some time in the whole day to unwind and just do…nothing.\r\n\r\nFinding a new hobby is probably the best way to spend all this newfound free time; a lot of them will even boost your résumé for those of you looking for that sort of thing. It allows you a way to not only learn a new skill, but to express yourself in your own little way that acts as a therapeutic measure against the maddening uniformity of this world. This is what I try to do and from my own experiences, it works.\r\n\r\nI for the matter of this discussion, am trying to learn a new programming language. You see, back during my final semester all of us had to submit a major project that showcased the knowledge and skills that we had picked up over the course of these last two years. I was one of the four students that took a project in embedded systems programming which is usually implemented using an Arduino micro-controller board. The Arduino uses a language eerily similar to another language called C, maybe you have heard of it somewhere. Now for the four of us, C was a language we had been using since we started learning to program so it was not like we had to learn a whole new language for our projects (we only had to learn a lifetime’s worth of electronics in about six months and some basic physics and engineering and all four of us probably lost a good twelve kilos or so just from the stress alone, but that is a story for another time). But the majority of the students in my class, considering the complexity of their projects along with the open-ended implementation goals they were given, chose a language known as Python for their projects (and by ‘majority’ I mean that in a class of around thirty students, only five or six did not use Python, including us four in Embedded Systems).\r\n\r\nNow for those of you who still remember their college days, you know it isn’t uncommon for students to ask each other for help during projects (as this is one of the many, many advantages of going to a traditional college, whatever the tier maybe: you get to be surrounded by people studying the same subject and who will probably end up working in the same field as you) as your professors may be too bogged down by administrative or research work to always be available to help you. So this was how it was for us as well, everyone was good friends with everyone else so all of us were vividly exposed to and familiar with the ideas and workings of each other’s projects. We would barter with each other by solving each other’s problems and this is how I was introduced to Python for the first time, by helping a classmate with some problems they were facing with their work.\r\n\r\nAfter a lifetime of dealing with the strict, immutable syntaxes of the languages I’ve used, the idea that a programming language can resemble basic human speech was too good for me to resist. So after everything was said and done, I sat down and began reading the documentation and watching tutorials online. I was able to get basic functionality in my codes within one week, that is how easy Python is: everything was just like a normal human language. The last two weeks I have spent learning this amazing new (I know, it was released decades ago but it is new for me) language seemed to go by in a blur and I rarely felt empty or lonely. Time just seemed to fly by; I would sit down at around 10 in the night and the next time I looked at the clock, it would be around 4 in the morning.\r\n\r\nBut as I said, this is not how I spend my entire day. I go out and meet my friends, I try to help them out with random errands, I make trips that I had been putting off, I finally started that DIY project that I had been promising myself I would start once college is over. I try to take as much time as I require to do all the things I want to do. Life isn’t a monotonous sequence of events that only flows in one direction. It is a tapestry with thousands of millions of interleaving twines criss-crossing and overlapping each other to form something beautiful.\r\n\r\nThis has of course been a personal example, everyone here might need to find their own hobbies to spend the time but I assure you that whatever you choose to spend your time doing, despite what some others might say, it will never be wasted time. Time spent learning new skills, developing a new hobby or just plain meeting new people or going to new places, even if they are it the town where you live, is never wasted. In this life, the greatest investment we can make is time and there are very few instances where this investment leads to a loss; all others lead to eventual personal gain, either material or emotional.\r\n\r\nWith that, I bid you all goodnight for now. I hope to see you all along with maybe a few new faces next time.	drama	2022-06-06 23:52:10.957832+05:30	2022-06-06 23:52:10.957832+05:30	da146a7f-4d77-4b62-b311-620ac5062a35
\.


--
-- TOC entry 3448 (class 0 OID 44521)
-- Dependencies: 219
-- Data for Name: userapp_user; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.userapp_user (password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, id, email, user_phone_primary, user_slug, user_type) FROM stdin;
pbkdf2_sha256$320000$Ens2rxGqOIT4us4nph4K95$LykHIE27jcT5HtiJl1u3wZQBz3B5ThGepA22y3+CNSE=	2022-06-06 23:00:28+05:30	t	admin	Admin	Superuser	t	t	2022-06-06 22:56:44+05:30	06f621c6-8a9a-41ea-8f14-0a0640f35cda	admin@admin.com	8811098879	admin-adminadmincom	user_admin
pbkdf2_sha256$320000$VeQ2NksZZQP4CLNBIOyTsP$kVog+MA5raTOsXZE+L7Hcc9cVo4kPA7aqjhr+KP5DoE=	\N	f	testuser_001	Test	User	f	t	2022-06-06 23:50:32.529187+05:30	da146a7f-4d77-4b62-b311-620ac5062a35	test_user_001@gmail.com	\N	testuser_001-test_user_001gmailcom	normal_user
pbkdf2_sha256$320000$vf6mrjecwQtyjlV9SRIueo$WHjJbXlPZqwZYcN3EqL7dyTShBXAhC/7mYN9nHa96ug=	\N	f	testuser_002	Test	User 002	f	t	2022-06-07 00:31:21.297355+05:30	209f33a7-3bc4-4ae6-b5db-d38f48ef5c1d	test_user_002@gmail.com	\N	testuser_002-test_user_002gmailcom	normal_user
\.


--
-- TOC entry 3450 (class 0 OID 44533)
-- Dependencies: 221
-- Data for Name: userapp_user_groups; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.userapp_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 3452 (class 0 OID 44540)
-- Dependencies: 223
-- Data for Name: userapp_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: prithoo
--

COPY public.userapp_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 215
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 217
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 213
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 36, true);


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 224
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 14, true);


--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 211
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 9, true);


--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 209
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 24, true);


--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 220
-- Name: userapp_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.userapp_user_groups_id_seq', 1, false);


--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 222
-- Name: userapp_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: prithoo
--

SELECT pg_catalog.setval('public.userapp_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3237 (class 2606 OID 44519)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 3242 (class 2606 OID 44505)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 3245 (class 2606 OID 44494)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3239 (class 2606 OID 44485)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3232 (class 2606 OID 44496)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 3234 (class 2606 OID 44478)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3274 (class 2606 OID 44604)
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- TOC entry 3276 (class 2606 OID 44606)
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- TOC entry 3270 (class 2606 OID 44587)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3227 (class 2606 OID 44471)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 3229 (class 2606 OID 44469)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3225 (class 2606 OID 44462)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3279 (class 2606 OID 44619)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3283 (class 2606 OID 44628)
-- Name: storyapp_story storyapp_story_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.storyapp_story
    ADD CONSTRAINT storyapp_story_pkey PRIMARY KEY (id);


--
-- TOC entry 3287 (class 2606 OID 44637)
-- Name: storyapp_story storyapp_story_title_author_id_90e08df5_uniq; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.storyapp_story
    ADD CONSTRAINT storyapp_story_title_author_id_90e08df5_uniq UNIQUE (title, author_id);


--
-- TOC entry 3248 (class 2606 OID 44531)
-- Name: userapp_user userapp_user_email_key; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user
    ADD CONSTRAINT userapp_user_email_key UNIQUE (email);


--
-- TOC entry 3258 (class 2606 OID 44538)
-- Name: userapp_user_groups userapp_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_groups
    ADD CONSTRAINT userapp_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3261 (class 2606 OID 44551)
-- Name: userapp_user_groups userapp_user_groups_user_id_group_id_809fade4_uniq; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_groups
    ADD CONSTRAINT userapp_user_groups_user_id_group_id_809fade4_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 3250 (class 2606 OID 44527)
-- Name: userapp_user userapp_user_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user
    ADD CONSTRAINT userapp_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3263 (class 2606 OID 44565)
-- Name: userapp_user_user_permissions userapp_user_user_permis_user_id_permission_id_2e646fa8_uniq; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_user_permissions
    ADD CONSTRAINT userapp_user_user_permis_user_id_permission_id_2e646fa8_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 3266 (class 2606 OID 44545)
-- Name: userapp_user_user_permissions userapp_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_user_permissions
    ADD CONSTRAINT userapp_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3255 (class 2606 OID 44529)
-- Name: userapp_user userapp_user_username_key; Type: CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user
    ADD CONSTRAINT userapp_user_username_key UNIQUE (username);


--
-- TOC entry 3235 (class 1259 OID 44520)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 3240 (class 1259 OID 44516)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 3243 (class 1259 OID 44517)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3230 (class 1259 OID 44502)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 3272 (class 1259 OID 44612)
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- TOC entry 3268 (class 1259 OID 44598)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 3271 (class 1259 OID 44599)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 3277 (class 1259 OID 44621)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 3280 (class 1259 OID 44620)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3281 (class 1259 OID 44638)
-- Name: storyapp_story_author_id_fe474d00; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX storyapp_story_author_id_fe474d00 ON public.storyapp_story USING btree (author_id);


--
-- TOC entry 3284 (class 1259 OID 44629)
-- Name: storyapp_story_slug_d721108a; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX storyapp_story_slug_d721108a ON public.storyapp_story USING btree (slug);


--
-- TOC entry 3285 (class 1259 OID 44630)
-- Name: storyapp_story_slug_d721108a_like; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX storyapp_story_slug_d721108a_like ON public.storyapp_story USING btree (slug varchar_pattern_ops);


--
-- TOC entry 3246 (class 1259 OID 44547)
-- Name: userapp_user_email_f366e595_like; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_email_f366e595_like ON public.userapp_user USING btree (email varchar_pattern_ops);


--
-- TOC entry 3256 (class 1259 OID 44563)
-- Name: userapp_user_groups_group_id_2c7413e1; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_groups_group_id_2c7413e1 ON public.userapp_user_groups USING btree (group_id);


--
-- TOC entry 3259 (class 1259 OID 44562)
-- Name: userapp_user_groups_user_id_1f2cef9b; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_groups_user_id_1f2cef9b ON public.userapp_user_groups USING btree (user_id);


--
-- TOC entry 3264 (class 1259 OID 44577)
-- Name: userapp_user_user_permissions_permission_id_d925323f; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_user_permissions_permission_id_d925323f ON public.userapp_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3267 (class 1259 OID 44576)
-- Name: userapp_user_user_permissions_user_id_83c73166; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_user_permissions_user_id_83c73166 ON public.userapp_user_user_permissions USING btree (user_id);


--
-- TOC entry 3251 (class 1259 OID 44548)
-- Name: userapp_user_user_slug_f3324da9; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_user_slug_f3324da9 ON public.userapp_user USING btree (user_slug);


--
-- TOC entry 3252 (class 1259 OID 44549)
-- Name: userapp_user_user_slug_f3324da9_like; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_user_slug_f3324da9_like ON public.userapp_user USING btree (user_slug varchar_pattern_ops);


--
-- TOC entry 3253 (class 1259 OID 44546)
-- Name: userapp_user_username_40e955dd_like; Type: INDEX; Schema: public; Owner: prithoo
--

CREATE INDEX userapp_user_username_40e955dd_like ON public.userapp_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3290 (class 2606 OID 44511)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3289 (class 2606 OID 44506)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3288 (class 2606 OID 44497)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3297 (class 2606 OID 44607)
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_userapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_userapp_user_id FOREIGN KEY (user_id) REFERENCES public.userapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3295 (class 2606 OID 44588)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3296 (class 2606 OID 44593)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_userapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_userapp_user_id FOREIGN KEY (user_id) REFERENCES public.userapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3298 (class 2606 OID 44631)
-- Name: storyapp_story storyapp_story_author_id_fe474d00_fk_userapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.storyapp_story
    ADD CONSTRAINT storyapp_story_author_id_fe474d00_fk_userapp_user_id FOREIGN KEY (author_id) REFERENCES public.userapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3292 (class 2606 OID 44557)
-- Name: userapp_user_groups userapp_user_groups_group_id_2c7413e1_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_groups
    ADD CONSTRAINT userapp_user_groups_group_id_2c7413e1_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3291 (class 2606 OID 44552)
-- Name: userapp_user_groups userapp_user_groups_user_id_1f2cef9b_fk_userapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_groups
    ADD CONSTRAINT userapp_user_groups_user_id_1f2cef9b_fk_userapp_user_id FOREIGN KEY (user_id) REFERENCES public.userapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3294 (class 2606 OID 44571)
-- Name: userapp_user_user_permissions userapp_user_user_pe_permission_id_d925323f_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_user_permissions
    ADD CONSTRAINT userapp_user_user_pe_permission_id_d925323f_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3293 (class 2606 OID 44566)
-- Name: userapp_user_user_permissions userapp_user_user_pe_user_id_83c73166_fk_userapp_u; Type: FK CONSTRAINT; Schema: public; Owner: prithoo
--

ALTER TABLE ONLY public.userapp_user_user_permissions
    ADD CONSTRAINT userapp_user_user_pe_user_id_83c73166_fk_userapp_u FOREIGN KEY (user_id) REFERENCES public.userapp_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2022-06-07 02:42:15

--
-- PostgreSQL database dump complete
--

